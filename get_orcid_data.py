import requests
import json
from diskcache import Cache

__all__ = ['ORCIDPublication', 'get_orcid_publications']

class ORCIDPublication:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)


orcid_cache = Cache('temp/orcid_cache')


# adapted from https://chrisholdgraf.com/blog/2022/orcid-auto-update/
def get_metadata_from_doi(doi):
    url = "https://dx.doi.org/" + str(doi)
    header = {'accept': 'application/citeproc+json'}
    r = requests.get(url, headers=header)
    if r.status_code!=200:
        return {}
    return json.loads(r.text)


def get_orcid_publications(user_id):
    if user_id in orcid_cache:
        return orcid_cache[user_id]
    resp = requests.get(f"https://pub.orcid.org/v2.0/{user_id}/works",
                        headers={'Accept':'application/orcid+json'})
    results = resp.json()
    publications = []
    titles = set()
    dois = set()
    for group in results['group']:
        work = group['work-summary'][0]
        putcode = work['put-code']
        work = requests.get(f"https://pub.orcid.org/v2.0/{user_id}/work/{putcode}", headers={'Accept':'application/orcid+json'}).json()
        title = work['title']['title']['value']
        pub = ORCIDPublication(
            title=title,
            date=int(work['publication-date']['year']['value']),
            type=work['type'],
            )
        if 'journal-title' in work and work['journal-title'] is not None and 'value' in work['journal-title']:
            pub.journal = work['journal-title']['value']
        doi = None
        for eid in work['external-ids']['external-id']:
            if eid['external-id-type'].lower()=='doi':
                doi = eid['external-id-value']
                pub.url = "http://dx.doi.org/"+doi
        missing_author_name = False
        if 'contributors' in work and 'contributor' in work['contributors'] and len(work['contributors']['contributor']):
            authors = []
            for contrib in work['contributors']['contributor']:
                if 'credit-name' not in contrib or contrib['credit-name'] is None:
                    authors.append("Name Missing")
                    # print(f"Missing author name in ORCID data for {title}")
                    missing_author_name = True
                else:
                    authors.append(contrib['credit-name']['value'])
            if len(authors)>6:
                authors = [authors[0], 'et al.']
            pub.authors = ', '.join(authors)
        # get metadata from the DOI and use that in preference if available
        if doi is not None:
            md = get_metadata_from_doi(doi)
            if 'title' in md:
                pub.title = title
            if 'container-title' in md:
                pub.journal = md['container-title']
            if 'issued' in md:
                pub.date = md["issued"]["date-parts"][0][0]
            if 'author' in md and len(md['author']):
                missing_author_name = False
                authors = []
                for auth in md['author']:
                    if 'ORCID' in auth:
                        authors.append(f'''<a href="{auth['ORCID']}">{auth['given']} {auth['family']}</a>''')
                    elif 'given' in auth and 'family' in auth:
                        authors.append(f'''{auth['given']} {auth['family']}''')
                    elif 'name' in auth:
                        authors.append(f'''{auth['name']}''')
                    elif 'literal' in auth:
                        authors.append(f'''{auth['literal']}''')
                    else:
                        authors.append("Name Missing")
                if len(authors)>6:
                    authors = [authors[0], 'et al.']
                pub.authors = ', '.join(authors)
        if missing_author_name:
            print(f"Missing author name in ORCID data for {title}")
        # Try to minimize duplicate entries that are found
        dup = False
        if title.lower() in titles:
            dup = True
        if doi is not None and doi.lower() in dois:
            dup = True
        if not dup:
            publications.append(pub)
        titles.add(title.lower())
        dois.add(doi.lower())
    orcid_cache.set(user_id, publications, expire=24*60*60)
    return publications
