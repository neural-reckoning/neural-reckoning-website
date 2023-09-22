import os, pickle, time, urllib
import http.client
from urllib.parse import urlparse

from templater import additional_urls


do_check_links = True

link_exceptions = set([
    'https://uk.linkedin.com/in/jean-hugues-lestang-90b70073', # LinkedIn doesn't like links... in...?
    'https://uk.linkedin.com/in/greta-horvathova-5a22961b1',
    ])


if os.path.exists('last_checked_links.pkl'):
    last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
else:
    last_checked_links = {}


today = time.strftime('%d/%m/%Y')
last_checked_links = dict((url, day) for url, day in last_checked_links.items() if day==today)
last_updated = time.strftime('%Y/%m/%d')


def check_link(url, msg):
    if url in last_checked_links or url in link_exceptions:
        return
    # first try just getting the header (quick)
    p = urlparse(url)
    conn = http.client.HTTPConnection(p.netloc)
    try:
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
    except Exception as ex:
        print('Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex))
        return
    if resp.status >= 400:
        try:
            # Pretend we are a browser because some journals refuse connections otherwise
            urllib.request.urlopen(urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }))
            last_checked_links[url] = today
        except Exception as ex:
            try:
                if hasattr(ex, 'getcode') and ex.getcode()==500: # just do a retry in this situation (internal server error)
                    ex.read()
                else:
                    raise
            except Exception as ex:
                print('Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex))
    else:
        last_checked_links[url] = today


def check_links():

    if do_check_links:
        
        # # Check publication URLs are OK
        # for publication in papers.values():
        #     for _, url in publication.urls:
        #         check_link(url, "publication "+publication.name)

        # Check all additions links are OK
        for url, pagename in additional_urls:
            check_link(url, "page "+pagename)

    pickle.dump(last_checked_links, open('last_checked_links.pkl', 'wb'))