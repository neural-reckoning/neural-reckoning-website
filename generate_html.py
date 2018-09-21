# -*- coding: utf-8 -*-
import os
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

check_links = True

if os.path.exists('last_checked_links.pkl'):
    last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
else:
    last_checked_links = {}

today = time.strftime('%d/%m/%Y')
last_checked_links = dict((url, day) for url, day in last_checked_links.iteritems() if day==today)

pages = OrderedDict([
    ('index.html', 'Home'),
    ('members.html', 'Members'),
    ('publications.html', 'Publications'),
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
        

env_globals = dict(pages=pages, publications=publications, hasattr=hasattr,
                   members=members, member_types=member_types,
                   member_publications=member_publications,
                   generate_email=generate_email, os=os,
                   category_id_names=category_id_names,
                   category_publications=category_publications,
                   category_id=category_id)

env = Environment(loader=FileSystemLoader('templates'),
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
    if url in last_checked_links:
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
