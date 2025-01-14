import requests
import json
from diskcache import Cache
import shelve

bluesky_cache = Cache('temp/bluesky_cache')

def get_bluesky_embed(url):
    if url in bluesky_cache:
        return bluesky_cache[url]
    resp = requests.get(f"https://embed.bsky.app/oembed",
                        params={'url': url, 'maxwidth': 400})
    results = resp.json()
    bluesky_cache.set(url, results['html'])
    return results['html']    

def get_bluesky_thread(urls):
    return '\n'.join([get_bluesky_embed(url) for url in urls])

def generate_bluesky_threads(papers):
    # generate bluesky threads for papers that have them
    for publication in papers.values():
        if hasattr(publication, 'bluesky_thread') and not hasattr(publication, 'bluesky_thread_html'):
            publication.bluesky_thread_html = get_bluesky_thread(publication.bluesky_thread)

if __name__=='__main__':
    print(get_bluesky_thread(['https://bsky.app/profile/did:plc:niqde7rkzo7ua3scet2rzyt7/post/3lfpcgulazs2y']))