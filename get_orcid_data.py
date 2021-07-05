import requests
import json

__all__ = ['ORCIDPublication', 'get_orcid_publications']

class ORCIDPublication:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)

def get_orcid_publications(user_id):
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
        if 'journal-title' in work:
            pub.journal = work['journal-title']['value']
        doi = None
        for eid in work['external-ids']['external-id']:
            if eid['external-id-type'].lower()=='doi':
                doi = eid['external-id-value']
                pub.url = "http://dx.doi.org/"+doi
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
    return publications
