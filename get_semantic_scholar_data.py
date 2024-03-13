from diskcache import Cache
import semanticscholar
import re

cache = Cache('temp/semantic_scholar_cache')

sch = semanticscholar.SemanticScholar(timeout=25)

class SemanticScholarPublication:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)


def get_semantic_scholar_publications(user_id):
    if user_id in cache:
        return cache[user_id]

    author = sch.get_author(user_id)

    publications = []
    all_papers = sch.get_papers([paper['paperId'] for paper in author['papers']])
    for paper in all_papers:
        # paper = sch.get_paper(paper['paperId'])
        pub = SemanticScholarPublication(
            title=paper['title'], date=paper['year']
            )
        if paper.url is not None:
            pub.url = paper['url']
        if paper.venue is not None:
            pub.journal = paper['venue']
        if paper.authors is not None:
            authors = []
            for author in paper['authors']:
                #authurl = author['url']
                authurl = f"https://www.semanticscholar.org/author/{author['authorId']}"
                authname = author['name']
                authors.append(f'<a href="{authurl}">{authname}</a>')
            if len(authors)>6:
                authors = [authors[0], 'et al.']
            pub.authors = ', '.join(authors)
        publications.append(pub)

    cache.set(user_id, publications, expire=24*60*60)
    return publications


if __name__=='__main__':
    get_semantic_scholar_publications(27620389)
