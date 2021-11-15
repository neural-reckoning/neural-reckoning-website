# # -*- coding: utf-8 -*-

# Standard library imports
import os

# External package imports
import yaml

# Local imports
from cache import save_cache
from categories import build_categories, write_categories
from people import get_people, write_people, make_people_thumbnails
from papers import get_papers, write_papers
from related import find_paper_authors
from software import get_software, write_software
from templater import update_template_globals
from twitter import generate_twitter_threads

# Load the basic navigational structure and put it into the template engine
nav = yaml.safe_load(open('navigation.yaml', 'r'))
update_template_globals(**nav)

# Load all the people, papers
people = get_people()
papers = get_papers()
software = get_software()

# Generate thumbnails
make_people_thumbnails(people)

# Generate twitter threads
generate_twitter_threads(papers)

# Find relationships
find_paper_authors(people, papers)
categories = build_categories(papers)

# Write all the people pages
write_people(people)
write_papers(papers)
write_categories(categories)
write_software(software)

# Copy static files to docs directory
os.system(r'copy files\* docs >nul')

# Save cache before finishing
save_cache()

# And we're done
print('Finished.')

#### CODE TO GENERATE YAML FILES FROM PYTHON #################################################

# import inspect, codecs
# yaml.SafeDumper.org_represent_str = yaml.SafeDumper.represent_str

# def repr_str(dumper, data):
#     if '\n' in data:
#         data = inspect.cleandoc(data)
#         if '\n' in data:
#             return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
#     return dumper.org_represent_str(data)

# yaml.add_representer(str, repr_str, Dumper=yaml.SafeDumper)

# from software import software
# for pub in software:
#     key = pub.name
#     md = {}
#     for k in ['title', 'url', 'logo', 'short', 'long', 'team']:
#         if k in pub.__dict__:
#             md[k] = getattr(pub, k)
#     for k, v in pub.__dict__.items():
#         if not k.startswith('_') and k not in md:
#             md[k] = v
#     del md['name']
#     basedir = 'software'
#     if not os.path.exists(basedir):
#         os.makedirs(basedir)
#     fname = os.path.join(basedir, key+'.yaml')
#     yaml.safe_dump(md, codecs.open(fname, 'w', encoding='utf-8'), allow_unicode=True, encoding='utf-8', sort_keys=False)


#################### OLD VERSION ############################################



# from get_semantic_scholar_data import get_semantic_scholar_publications
# import os, sys
# from jinja2 import Environment, FileSystemLoader, select_autoescape
# from collections import OrderedDict, defaultdict
# import urllib.request
# import urllib.error
# import urllib.parse
# from copy import copy
# import pickle
# import time
# import re
# import codecs
# from wordcloud import WordCloud
# import json
# import hashlib
# from PIL import Image, ImageDraw

# from publications import publications, category_inclusions, category_detail_links
# from software import software
# from members import members, member_types, member_dict
# from email_addresses import generate_email
# from link_exceptions import link_exceptions
# from get_orcid_data import get_orcid_publications
# from get_semantic_scholar_data import get_semantic_scholar_publications

# check_links = True

# if os.path.exists('last_checked_links.pkl'):
#     last_checked_links = pickle.load(open('last_checked_links.pkl', 'rb'))
# else:
#     last_checked_links = {}

# today = time.strftime('%d/%m/%Y')
# last_checked_links = dict((url, day) for url, day in last_checked_links.items() if day==today)
# last_updated = time.strftime('%Y/%m/%d')


# # Process software page data
# for sw in software:
#     if not hasattr(sw, 'urls'):
#         sw.urls = []
#     sw.urls = [('Homepage', sw.url)]+sw.urls
#     sw.team_ids = []
#     for auth in sw.team:
#         authid = authname_to_member_id.get(auth, 'placeholder')
#         sw.team_ids.append(authid)
#         if authid!="placeholder":
#             mem = member_dict[authid]
#             if not hasattr(mem, 'software'):
#                 mem.software = []
#             mem.software.append(sw)

# env_globals = dict(pages=pages, publications=publications, hasattr=hasattr,
#                    software=software,
#                    last_updated=last_updated,
#                    members=members, member_types=member_types, member_dict=member_dict,
#                    member_publications=member_publications,
#                    generate_email=generate_email, os=os,
#                    category_id_names=category_id_names,
#                    category_publications=category_publications,
#                    category_id=category_id,
#                    cached=cached,
#                    unindexed_pages=unindexed_pages)

# # Generate index pages
# for filename, title in list(pages.items())+list(unindexed_pages.items()):
#     if os.path.exists(os.path.join('templates', filename)):
#         page = env.get_template(filename).render(title=title, filename=filename)
#         codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))

# # Generate publication categories
# for catid, catname in list(category_id_names.items()):
#     filename = 'publication_category_%s.html' % catid
#     page = env.get_template('publication_category.html').render(
#                 publications=category_publications(catid),
#                 category_name=catname,
#                 title=catname, filename=filename,
#                 detail_link=category_detail_links.get(catid, None),
#                 )
#     codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))
    
    
# # Generate software pages
# for sw in software:
#     filename = "sw_"+sw.name+".html"
#     page = env.get_template('single_software.html').render(sw=sw, filename=filename)
#     codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))

# import http.client
# from urllib.parse import urlparse

# def check_link(url, msg):
#     if url in last_checked_links or url in link_exceptions:
#         return
#     # first try just getting the header (quick)
#     p = urlparse(url)
#     conn = http.client.HTTPConnection(p.netloc)
#     try:
#         conn.request('HEAD', p.path)
#         resp = conn.getresponse()
#     except Exception as ex:
#         print('Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex))
#         return
#     if resp.status >= 400:
#         try:
#             # Pretend we are a browser because some journals refuse connections otherwise
#             urllib.request.urlopen(urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }))
#             last_checked_links[url] = today
#         except Exception as ex:
#             try:
#                 if hasattr(ex, 'getcode') and ex.getcode()==500: # just do a retry in this situation (internal server error)
#                     ex.read()
#                 else:
#                     raise
#             except Exception as ex:
#                 print('Failed: {msg}, URL {url}, exception {ex}'.format(msg=msg, url=url, ex=ex))
#     else:
#         last_checked_links[url] = today


# if check_links:
#     print('Finished generating HTML, now checking links.')
    
#     # Check publication URLs are OK
#     for publication in publications:
#         for _, url in publication.urls:
#             check_link(url, "publication "+publication.name)

#     # Check all additions links are OK
#     for url, pagename in additional_urls:
#         check_link(url, "page "+pagename)

# pickle.dump(last_checked_links, open('last_checked_links.pkl', 'wb'))