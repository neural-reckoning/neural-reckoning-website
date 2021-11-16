# # -*- coding: utf-8 -*-

# Standard library imports
import os

# External package imports
import yaml

# Local imports
from cache import save_cache
from categories import build_categories, write_categories
from links import check_links
from people import get_people, write_people, make_people_thumbnails
from pages import write_pages
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
write_pages(nav, people, papers, software, categories)

# Copy static files to docs directory
os.system(r'copy files\* docs >nul')

# Save cache before finishing
save_cache()

# Check links
print('Finished generating HTML, now checking links.')
check_links()

# And we're done
print('Finished.')

#################### OLD VERSION ############################################

# import urllib.request
# import urllib.error
# import urllib.parse
# from wordcloud import WordCloud
# import hashlib
# from PIL import Image, ImageDraw