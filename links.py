import os, pickle, time, urllib
import http.client
from urllib.parse import urlparse
from diskcache import Cache

from templater import additional_urls

cache_expiry_seconds = 7*24*60*60  # 7 days in seconds
failed_link_cache_expiry_seconds = 60*60  # 1 hour in seconds

cache = Cache('temp/link_check_cache')

do_check_links = True

link_exceptions = set([
    'https://www.cns.nyu.edu/malab/bayesianbook.html', # This one just seems to not respond when I check it via python, but works fine
    ])


# # # if os.path.exists('last_checked_links.pkl'):
# # #     last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
# # # else:
# # #     last_checked_links = {}


# # today = time.strftime('%d/%m/%Y')
# # last_checked_links = dict((url, day) for url, day in last_checked_links.items() if day==today)
# # last_updated = time.strftime('%Y/%m/%d')

# checked_this_run = set()


def check_link(url, msg):
    if url in cache or url in link_exceptions:
        return
    if 'https://t.co/' in url:
        return
    if 'linkedin.com' in url:
        return
    if 'biorxiv.org' in url:
        return # rate limiting, and they're likely to be correct
    # first try just getting the header (quick)
    p = urlparse(url)
    conn = http.client.HTTPConnection(p.netloc, timeout=5)
    try:
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
    except Exception as ex:
        failure_message = 'Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex)
        print(failure_message)
        cache.set(url, failure_message, expire=failed_link_cache_expiry_seconds)
        return
    if resp.status >= 400:
        try:
            # Pretend we are a browser because some journals refuse connections otherwise
            urllib.request.urlopen(urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }), timeout=5)
            cache.set(url, True, expire=cache_expiry_seconds)
        except Exception as ex:
            try:
                if hasattr(ex, 'getcode') and ex.getcode()==500: # just do a retry in this situation (internal server error)
                    ex.read()
                else:
                    raise
            except Exception as ex:
                failure_message = 'Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex)
                print(failure_message)
                cache.set(url, failure_message, expire=failed_link_cache_expiry_seconds)
    else:
        cache.set(url, True, expire=cache_expiry_seconds)


def check_links():

    if do_check_links:
        
        # # Check publication URLs are OK
        # for publication in papers.values():
        #     for _, url in publication.urls:
        #         check_link(url, "publication "+publication.name)

        # Check all additions links are OK
        for url, pagename in additional_urls:
            check_link(url, "page "+pagename)

        # Print out any failed links
        for url, pagename in additional_urls:
            if url in cache and cache[url] is not True:
                print(cache[url])
