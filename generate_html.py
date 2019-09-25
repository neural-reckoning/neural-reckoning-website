# -*- coding: utf-8 -*-
import os, sys
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict
import urllib2
from copy import copy
import pickle
import time
import re
import codecs

from publications import publications, category_inclusions, category_detail_links
from members import members, member_types
from email import generate_email
from link_exceptions import link_exceptions

check_links = True

if os.path.exists('last_checked_links.pkl'):
    last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
else:
    last_checked_links = {}

today = time.strftime('%d/%m/%Y')
last_checked_links = dict((url, day) for url, day in last_checked_links.iteritems() if day==today)
last_updated = time.strftime('%Y/%m/%d')

pages = OrderedDict([
    ('index.html', 'Home'),
    ('members.html', 'Members'),
    ('publications.html', 'Publications'),
    ('themes.html', 'Themes'),
    ('software.html', 'Software'),
    ('openings.html', 'Openings'),
    ('location.html', 'Location'),
    ])

unindexed_pages = {
    'neuroinformatics.html': 'Neuroinformatics',
    'sensory.html': 'Sensory neuroscience',
    'mathematics.html': 'Mathematics',
    }


def member_publications(member):
    newpubs = []
    for publication in publications:
        for auth in member.author_names:
            if auth in publication.authors:
                newpubs.append(publication)
                break
    return newpubs


# Generate links to member pages in publications
for member in members:
    for publication in publications:
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


def category_id(name):
    return name.lower().replace(' ', '')


# generate inclusions and category ids for publications
category_id_inclusions = {}
category_id_names = {}
for name, inc in category_inclusions.items():
    catid = category_id(name)
    category_id_names[catid] = name
    category_id_inclusions[catid] = set([])
    inc = copy(inc)
    while len(inc):
        curname, inc = inc[0], inc[1:]
        category_id_inclusions[catid].add(category_id(curname))
        if curname in category_inclusions:
            inc.extend(category_inclusions[curname])
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
for k, v in category_detail_links.items():
    category_detail_links[category_id(k)] = v
                

def category_publications(catid):
    pubs = []
    for pub in publications:
        if catid in pub.category_ids:
            pubs.append(pub)
    return pubs

# Generate category graphs and HTML maps
from collections import defaultdict
numpapers = defaultdict(int)
category_graph = {}
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
for catname, inclusions in category_inclusions.items():
    tgt_id = category_id(catname)
    for inclusion in inclusions:
        src_id = category_id(inclusion)
        category_graph[src_id].add(tgt_id)
# Generate hierarchical categories
category_dot_lines = []
category_colours = {}
for cat_id in category_graph.keys():
    cat_name = category_id_names[cat_id]
    col = 0.7-0.7*(numpapers[cat_id]-min_num_papers)/(1.0*(max_num_papers-min_num_papers))
    col = int(255.0*col)
    col = ('%.02X' % col)*3
    col = '#'+col
    category_colours[cat_id] = col
    category_dot_lines.append('{cat_id} [URL="publication_category_{cat_id}.html", label="{cat_name}", color="{col}", fontcolor="{col}", '
                              'shape=box];'.format(cat_id=cat_id, cat_name=cat_name, col=col))
for src_id, target_ids in category_graph.items():
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
for (cat_id_1, cat_id_2), nc in category_connections.items():
    col = 0.9-0.9*(nc-min_connections)/(1.0*(max_connections-min_connections))
    col = int(255.0*col)
    col = ('%.02X' % col)*3
    col = '#'+col
    category_dot_lines.append(
        '    {cat_id_1} -- {cat_id_2} [len={edgelen}, color="{col}"]'.format(cat_id_1=cat_id_1, cat_id_2=cat_id_2, nc=nc,
                                                                             col=col, edgelen=1.0/(max_connections/2+nc)))
for cat_id in category_graph.keys():
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


# wordcloud: explicitly delete docs/wordcloud.png to recalculate
if not os.path.exists('docs/wordcloud.png'):
    try:
        from wordcloud import WordCloud
        all_abstracts = ' '.join(getattr(pub, 'abstract', '') for pub in publications)
        wordcloud = WordCloud(background_color="white", width=1000, height=600).generate(all_abstracts)
        wordcloud.to_file('docs/wordcloud.png')
    except ImportError:
        pass


env_globals = dict(pages=pages, publications=publications, hasattr=hasattr,
                   last_updated=last_updated,
                   members=members, member_types=member_types,
                   member_publications=member_publications,
                   generate_email=generate_email, os=os,
                   category_id_names=category_id_names,
                   category_publications=category_publications,
                   category_id=category_id)

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
for filename, title in pages.items()+unindexed_pages.items():
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
for catid, catname in category_id_names.items():
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
    
# Copy static files to docs directory
os.system(r'copy files\* docs >nul')

import httplib
from urlparse import urlparse

def check_link(url, msg):
    if url in last_checked_links or url in link_exceptions:
        return
    # first try just getting the header (quick)
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    if resp.status >= 400:
        try:
            # Pretend we are a browser because some journals refuse connections otherwise
            urllib2.urlopen(urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }))
            last_checked_links[url] = today
        except Exception as ex:
            try:
                if hasattr(ex, 'getcode') and ex.getcode()==500: # just do a retry in this situation (internal server error)
                    ex.read()
                else:
                    raise
            except Exception as ex:
                print 'Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex)
    else:
        last_checked_links[url] = today


if check_links:
    print 'Finished generating HTML, now checking links.'
    
    # Check publication URLs are OK
    for publication in publications:
        for _, url in publication.urls:
            check_link(url, "publication "+publication.name)

    # Check all additions links are OK
    for url, pagename in additional_urls:
        check_link(url, "page "+pagename)

pickle.dump(last_checked_links, open('last_checked_links.pkl', 'wb'))

print 'Finished.'