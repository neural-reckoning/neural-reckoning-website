from diskcache import Cache
import semanticscholar
import time
import tenacity

cache = Cache('temp/semantic_scholar_cache')

sch = semanticscholar.SemanticScholar(timeout=25) # note: rate limit is 100 requests per 5 minutes

class SemanticScholarPublication:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)

# Semantic scholar seems to hit rate limits very quickly, so this caches as much as possible
# in order to make retrying less painful.
def get_papers(paper_ids):
    papers_not_in_cache = set(paper_ids).difference(list(cache.iterkeys()))
    if papers_not_in_cache:
        time.sleep(3)
        print(f"Getting papers from semantic scholar with ids: {paper_ids}")
        try:
            papers = sch.get_papers(list(papers_not_in_cache))
            for paper in papers:
                cache.set(paper['paperId'], paper, expire=24*60*60)
        except tenacity.RetryError:
            print("Connection refused. Sleeping for 10 seconds.")
            time.sleep(10)
            papers = []
            for paper_id in papers_not_in_cache:
                paper = sch.get_paper(paper_id)
                cache.set(paper_id, paper, expire=24*60*60)
    return [cache[paper_id] for paper_id in paper_ids]


def get_semantic_scholar_publications(user_id):
    if user_id in cache:
        return cache[user_id]

    if f'scholar_{user_id}' not in cache:
        time.sleep(3)
        print(f"Getting data for semantic scholar user {user_id}")
        author = sch.get_author(user_id)
        cache.set(f'scholar_{user_id}', author, expire=24*60*60)
    else:
        author = cache[f'scholar_{user_id}']

    publications = []
    time.sleep(3)
    paper_ids = [paper['paperId'] for paper in author['papers']]
    all_papers = get_papers(paper_ids)
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
