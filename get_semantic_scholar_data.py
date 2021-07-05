from diskcache import Cache
import semanticscholar as sch


cache = Cache('temp/semantic_scholar_cache')


class SemanticScholarPublication:
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)


def get_semantic_scholar_publications(user_id):
    if user_id in cache:
        return cache[user_id]

    author = sch.author(user_id, timeout=2)

    publications = []
    for paper in author['papers']:
        paper = sch.paper(paper['paperId'], timeout=2)
        pub = SemanticScholarPublication(
            title=paper['title'], date=paper['year']
            )
        if 'url' in paper:
            pub.url = paper['url']
        if 'venue' in paper:
            pub.journal = paper['venue']
        publications.append(pub)

    cache.set(user_id, publications, expire=24*60*60)
    return publications


if __name__=='__main__':
    get_semantic_scholar_publications(27620389)
