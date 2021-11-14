# -*- coding: utf-8 -*-
from get_semantic_scholar_data import get_semantic_scholar_publications
import os, sys
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict, defaultdict
import urllib.request
import urllib.error
import urllib.parse
from copy import copy
import pickle
import time
import re
import codecs
from wordcloud import WordCloud
import json
import hashlib
from PIL import Image, ImageDraw
import tweepy
from twitter_secrets import api_key, api_secret_key
import shelve

from publications import publications, category_inclusions, category_detail_links
from software import software
from members import members, member_types, member_dict
from email_addresses import generate_email
from link_exceptions import link_exceptions
from get_orcid_data import get_orcid_publications
from get_semantic_scholar_data import get_semantic_scholar_publications

check_links = True

if os.path.exists('last_checked_links.pkl'):
    last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
else:
    last_checked_links = {}

if os.path.exists('cached.json'):
    cached = json.load(open('cached.json', 'r'))
else:
    cached = {}

today = time.strftime('%d/%m/%Y')
last_checked_links = dict((url, day) for url, day in last_checked_links.items() if day==today)
last_updated = time.strftime('%Y/%m/%d')

pages = OrderedDict([
    ('index.html', 'Home'),
    ('members.html', 'Members'),
    ('publications.html', 'Publications'),
    ('themes.html', 'Themes'),
    ('software.html', 'Software'),
    ('openings.html', 'Join us'),
    ('location.html', 'Location'),
    ])

unindexed_pages = OrderedDict([
    ('comp-neuro-resources.html', 'Computational neuroscience resources'),
    ('neuroinformatics.html', 'Neuroinformatics'),
    ('sensory.html', 'Sensory neuroscience'),
    ('mathematics.html', 'Mathematics'),
    ('apply_phd.html', 'PhD application process'),
    ('accessibility.html', 'Accessibility statement'),
    ])


def member_publications(member):
    newpubs = []
    for publication in publications:
        for auth in member.author_names:
            if auth in publication.authors:
                newpubs.append(publication)
                break
    return newpubs

# Generate member thumbnails
medium = 100
small = 75
def add_transparent_circle(im):
    w, h = im.size
    mask = Image.new("L", (w*5, h*5), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, w*5, h*5), fill=255)
    mask = mask.resize((w, h))
    im.putalpha(mask)
photo_fnames = [
    #('files/portrait_placeholder', '.png')
    ]
for member in members:
    photo_fnames.append(('files/photo_'+member.id, '.jpg'))
for base, ext in photo_fnames:
    if os.path.exists(base+ext):
        try:
            with Image.open(base+ext) as im:
                # medium size thumbnail is just square
                im_medium = im.copy()
                im_medium.thumbnail((medium, medium))
                #im_medium.save(base+'.m.jpg')
                add_transparent_circle(im_medium)
                im_medium.save(base+'.m.circ.png')
                # small thumbnail is circle
                im_small = im.copy()
                im_small.thumbnail((small, small))
                #im_small.save(base+'.s.jpg')
                add_transparent_circle(im_small)
                im_small.save(base+'.s.circ.png')
        except OSError:
            print('Cannot create thumbnail for', base)

# Get ORCID/SemanticScholar publications
for member in members:
    if hasattr(member, 'orcid'):
        member.external_publications = get_orcid_publications(member.orcid)
    elif hasattr(member, 'semantic_scholar'):
        member.external_publications = get_semantic_scholar_publications(member.semantic_scholar)

# Generate list of publication author names and ids
authname_to_member_id = {}
for member in members:
    for memname in member.author_names:
        authname_to_member_id[memname] = member.id
for publication in publications:
    pubauths = [a.strip() for a in publication.authors.split(',')]
    author_names_and_ids = []
    author_ids = []
    for pubauth in pubauths:
        authid = authname_to_member_id.get(pubauth, 'placeholder')
        author_names_and_ids.append((pubauth, authid))
        author_ids.append(authid)
    publication.author_names_and_ids = author_names_and_ids
    publication.author_ids = author_ids

# Generate links to member pages in publications
for member in members:
    for publication in publications:
        publication.year = str(publication.year)
        pubauths = [a.strip() for a in publication.authors.split(',')]
        newpubauths = []
        for pubauth in pubauths:
            if pubauth in member.author_names:
                pubauth = '''<a href="{member.id}.html">{pubauth}</a>'''.format(member=member, pubauth=pubauth)
            newpubauths.append(pubauth)
        publication.authors = ', '.join(newpubauths)
        if not hasattr(publication, 'authors_list_text'):
            publication.authors_list_text = pubauths
        if len(pubauths)<=6:
            publication.authors_short = publication.authors
            publication.authors_short_list_text = publication.authors_list_text
        else:
            publication.authors_short = pubauths[0]+', et al.'
            publication.authors_short_list_text = [pubauths[0], 'et al.']

# generate icons for links in publications
for publication in publications:
    new_urls = []
    icons = {}
    for (name, url) in publication.urls:
        if re.search(r'\bvideo\b', name, flags=re.IGNORECASE):
            name = '<i class="fa fa-video-camera"></i> '+name
            if 'video' not in icons: # only use the first video link
                icons['video'] = f'''
                    <a href="{url}" target="_blank">
                        <i class="fa fa-video-camera"></i>
                    </a>
                    '''
        if re.search(r'\bpdf\b', name, flags=re.IGNORECASE):
            name = '<i class="fa fa-file-pdf-o"></i> '+name
            if 'pdf' not in icons or 'preprint' in name.lower(): # use first pdf link or preprint version
                icons['pdf'] = f'''
                    <a href="{url}" target="_blank">
                        <i class="fa fa-file-pdf-o"></i>
                    </a>
                    '''
        if re.search(r'\b(twitter|tweeprint)\b', name, flags=re.IGNORECASE):
            name = '<i class="fa fa-twitter"></i> '+name
            if 'twitter' not in icons: # use first twitter link
                icons['twitter'] = f'''
                    <a href="{url}" target="_blank">
                        <i class="fa fa-twitter"></i>
                    </a>
                    '''
        if re.search(r'\bhtml\b', name, flags=re.IGNORECASE):
            name = '<i class="fa fa-newspaper-o"></i> '+name
            if 'html' not in icons: # use first html link
                icons['html'] = f'''
                    <a href="{url}" target="_blank">
                        <i class="fa fa-newspaper-o"></i>
                    </a>
                    '''
        new_urls.append((name, url))
    publication.urls = new_urls
    publication.icons_dict = icons
    publication.icons = ''.join([icon_html for icon_type, icon_html in sorted(icons.items(), reverse=True)])


# generate twitter threads for papers that have them
twitter_api = None
def get_twitter_api():
    global twitter_api
    if twitter_api is None:
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        twitter_api = tweepy.API(auth)
with shelve.open('twitter_threads_cache') as twitter_threads:
    for publication in publications:
        if hasattr(publication, 'last_tweet_in_thread'):
            if publication.last_tweet_in_thread in twitter_threads:
                publication.twitter_thread = twitter_threads[publication.last_tweet_in_thread]
            else:
                get_twitter_api()
                i = publication.last_tweet_in_thread
                tweets = []
                omit = 0
                while i is not None:
                    s = twitter_api.get_status(i)
                    embed = twitter_api.get_oembed('https://twitter.com/twitter/statuses/'+s.id_str, hide_thread=1, omit_script=omit, dnt=1, maxwidth=400)
                    tweets.append(embed)
                    i = s.in_reply_to_status_id
                    omit = 1
                html = ''.join(embed['html'] for embed in tweets[::-1])
                publication.twitter_thread = html
                twitter_threads[publication.last_tweet_in_thread] = html


def category_id(name):
    return name.lower().replace(' ', '')

# generate inclusions and category ids for publications
all_categories = set(list(category_inclusions.keys())+[cat for inc in list(category_inclusions.values()) for cat in inc])
for pub in publications:
    for cat in pub.categories:
        all_categories.add(cat)
category_id_inclusions = defaultdict(list)
category_id_names = {}
# recursively fill in all inclusions
def recursive_inclusions(name):
    inc = set(category_inclusions.get(name, []))
    for name in inc:
        inc = inc.union(recursive_inclusions(name))
    return inc
for name in all_categories:
    catid = category_id(name)
    category_id_names[catid] = name
    category_id_inclusions[catid] = set([category_id(n) for n in recursive_inclusions(name)])
for pub in publications:
    names = pub.categories
    pub.category_ids = set([])
    for name in names:
        catid = category_id(name)
        category_id_names[catid] = name
        pub.category_ids.add(catid)
        if catid in category_id_inclusions:
            for cid in category_id_inclusions[catid]:
                pub.category_ids.add(cid)
for k, v in list(category_detail_links.items()):
    category_detail_links[category_id(k)] = v
                

def category_publications(catid):
    pubs = []
    for pub in publications:
        if catid in pub.category_ids:
            pubs.append(pub)
    return pubs

# Generate category graphs and HTML maps
numpapers = defaultdict(int)
category_graph = defaultdict(set)
category_connections = defaultdict(int)
for pub in publications:
    for cat in pub.category_ids:
        category_graph[cat] = set([])
        numpapers[cat] += 1
        for cat2 in pub.category_ids:
            if cat2<cat:
                category_connections[cat, cat2] += 1
max_connections = max(category_connections.values())
min_connections = min(category_connections.values())
max_num_papers = max(numpapers.values())
min_num_papers = min(numpapers.values())
for catname, inclusions in list(category_inclusions.items()):
    tgt_id = category_id(catname)
    for inclusion in inclusions:
        src_id = category_id(inclusion)
        category_graph[src_id].add(tgt_id)
# Generate hierarchical categories
category_dot_lines = []
category_colours = {}
for cat_id in list(category_graph.keys()):
    cat_name = category_id_names[cat_id]
    col = 0.7-0.7*(numpapers[cat_id]-min_num_papers)/(1.0*(max_num_papers-min_num_papers))
    col = int(255.0*col)
    col = ('%.02X' % col)*3
    col = '#'+col
    category_colours[cat_id] = col
    category_dot_lines.append('{cat_id} [URL="publication_category_{cat_id}.html", label="{cat_name}", color="{col}", fontcolor="{col}", '
                              'shape=box];'.format(cat_id=cat_id, cat_name=cat_name, col=col))
for src_id, target_ids in list(category_graph.items()):
    for tgt_id in target_ids:
        category_dot_lines.append('{src_id} -> {tgt_id} [color="{col}"];'.format(src_id=src_id, tgt_id=tgt_id,
                                                                                 col=category_colours[tgt_id]))
category_dot = '''
digraph categories_hierarchy {{
    rankdir = LR;
{graphspec}
}}
'''.format(graphspec='\n'.join(category_dot_lines))
if not os.path.exists('temp'):
    os.mkdir('temp')
open('temp/categories_hierarchy.dot', 'w').write(category_dot)
layout_algo = 'dot'
if os.system('{algo} -Tsvg temp/categories_hierarchy.dot -o temp/categories_hierarchy.svg'.format(algo=layout_algo))==0:
    svg = open('temp/categories_hierarchy.svg', 'r').read()
    svg = svg.replace('<svg', '<svg class="img-fluid"')
    open('temp/categories_hierarchy.svg', 'w').write(svg)
# Spontaneous category graph
category_dot_lines = []
for (cat_id_1, cat_id_2), nc in list(category_connections.items()):
    col = 0.9-0.9*(nc-min_connections)/(1.0*(max_connections-min_connections))
    col = int(255.0*col)
    col = ('%.02X' % col)*3
    col = '#'+col
    category_dot_lines.append(
        '    {cat_id_1} -- {cat_id_2} [len={edgelen}, color="{col}"]'.format(cat_id_1=cat_id_1, cat_id_2=cat_id_2, nc=nc,
                                                                             col=col, edgelen=1.0/(max_connections/2+nc)))
for cat_id in list(category_graph.keys()):
    cat_name = category_id_names[cat_id]
    col = category_colours[cat_id]
    category_dot_lines.append(
        '    {cat_id} [URL="publication_category_{cat_id}.html", label="{cat_name}", color="{col}", fontcolor="{col}", shape=box];'.format(
            cat_id=cat_id, cat_name=cat_name, col=col))
category_dot = '''
graph categories_spontaneous {{
    overlap=scale; splines=true;
{graphspec}
}}
'''.format(graphspec='\n'.join(category_dot_lines))
category_dot.replace('<svg', '<svg class="img-fluid" ')
open('temp/categories_spontaneous.dot', 'w').write(category_dot)
layout_algo = 'neato'
if os.system('{algo} -Tsvg temp/categories_spontaneous.dot -o temp/categories_spontaneous.svg'.format(algo=layout_algo))==0:
    svg = open('temp/categories_spontaneous.svg', 'r').read()
    svg = svg.replace('<svg', '<svg class="img-fluid"')
    open('temp/categories_spontaneous.svg', 'w').write(svg)
else:
    print("Couldn't run categories spontaneous dot")


# wordcloud: explicitly delete docs/wordcloud.png to recalculate
def make_wordcloud(member=None, width=350, height=350):
    if member is None:
        fname = 'docs/wordcloud.png'
    else:
        fname = 'docs/wordcloud_{author}.png'.format(author=member.id)
    if member is None:
        mpubs = publications
    else:
        mpubs = member_publications(member)
    if len(mpubs)==0:
        return
    all_abstracts = ' '.join(getattr(pub, 'abstract', '') for pub in mpubs)
    m = hashlib.md5()
    m.update(all_abstracts.encode("utf-8"))
    abstract_hash = m.hexdigest()
    if os.path.exists(fname) and fname in cached and cached[fname]==abstract_hash:
        return
    print('recomputing wordcloud', (member.name if member is not None else 'all'))
    wordcloud = WordCloud(background_color="white", width=width, height=height).generate(all_abstracts)
    wordcloud.to_file(fname)
    cached[fname] = abstract_hash

make_wordcloud(width=1000, height=400)
for member in members:
    make_wordcloud(member)

# Process software page data
for sw in software:
    if not hasattr(sw, 'urls'):
        sw.urls = []
    sw.urls = [('Homepage', sw.url)]+sw.urls
    sw.team_ids = []
    for auth in sw.team:
        authid = authname_to_member_id.get(auth, 'placeholder')
        sw.team_ids.append(authid)
        if authid!="placeholder":
            mem = member_dict[authid]
            if not hasattr(mem, 'software'):
                mem.software = []
            mem.software.append(sw)

env_globals = dict(pages=pages, publications=publications, hasattr=hasattr,
                   software=software,
                   last_updated=last_updated,
                   members=members, member_types=member_types, member_dict=member_dict,
                   member_publications=member_publications,
                   generate_email=generate_email, os=os,
                   category_id_names=category_id_names,
                   category_publications=category_publications,
                   category_id=category_id,
                   cached=cached,
                   unindexed_pages=unindexed_pages)

env = Environment(loader=FileSystemLoader(['templates', 'temp']),
                  trim_blocks=True,
                  lstrip_blocks=True,
                  )
env.globals.update(env_globals)

additional_urls = []
def scan_html_for_links(page, name):
    for url in re.findall('''href\s*=\s*["']\s*(http.*?)\s*["']''', page):
        additional_urls.append((url, name))
    return page

# Generate index pages
for filename, title in list(pages.items())+list(unindexed_pages.items()):
    if os.path.exists(os.path.join('templates', filename)):
        page = env.get_template(filename).render(title=title, filename=filename)
        codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))

# Generate publications
for publication in publications:
    filename = 'pub_'+publication.name+'.html'
    page = env.get_template('single_publication.html').render(
                                publication=publication,
                                title=publication.title, filename=filename)
    codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))
    
# Generate publication categories
for catid, catname in list(category_id_names.items()):
    filename = 'publication_category_%s.html' % catid
    page = env.get_template('publication_category.html').render(
                publications=category_publications(catid),
                category_name=catname,
                title=catname, filename=filename,
                detail_link=category_detail_links.get(catid, None),
                )
    codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))
    
    
# Generate members
for member in members:
    filename = member.id+'.html'
    page = env.get_template('single_member.html').render(
                                member=member,
                                title=member.name, filename=filename)
    codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))

# Generate software pages
for sw in software:
    filename = "sw_"+sw.name+".html"
    page = env.get_template('single_software.html').render(sw=sw, filename=filename)
    codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))

# Copy static files to docs directory
os.system(r'copy files\* docs >nul')

import http.client
from urllib.parse import urlparse

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


if check_links:
    print('Finished generating HTML, now checking links.')
    
    # Check publication URLs are OK
    for publication in publications:
        for _, url in publication.urls:
            check_link(url, "publication "+publication.name)

    # Check all additions links are OK
    for url, pagename in additional_urls:
        check_link(url, "page "+pagename)

pickle.dump(last_checked_links, open('last_checked_links.pkl', 'wb'))
json.dump(cached, open('cached.json', 'w'), sort_keys=True, indent=4)

print('Finished.')