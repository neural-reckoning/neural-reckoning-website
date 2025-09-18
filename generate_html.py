# # -*- coding: utf-8 -*-

# Standard library imports
import os

# External package imports
import yaml

# Local imports
from bluesky import generate_bluesky_threads
from cache import save_cache
from categories import build_categories, write_categories
from links import check_links
from organisations import get_organisations, write_organisations
from people import get_people, write_people, make_people_thumbnails
from pages import write_pages, make_members_global_for_navigation
from papers import get_papers, write_papers
from related import find_thing_authors, find_related, RelatedSoftwareGetter, RelatedThingGetter
from search import generate_json_for_search
from software import get_software, write_software
from templater import update_template_globals
from twitter import generate_twitter_threads
from videos import get_videos, write_videos
from wordclouds import make_wordclouds

# Load the basic navigational structure and put it into the template engine
nav = yaml.safe_load(open('navigation.yaml', 'r'))
update_template_globals(**nav)

# Load all the people, papers
people = get_people()
papers = get_papers()
software = get_software()
videos = get_videos()
organisations = get_organisations()
generate_json_for_search(papers)

# Generate thumbnails
make_people_thumbnails(people)

# Generate social media threads
generate_twitter_threads(papers)
generate_bluesky_threads(papers)

# Find relationships
find_thing_authors(people, papers)
find_thing_authors(people, software)
categories = build_categories({**papers, **software, **videos, **organisations})
find_related(papers, RelatedSoftwareGetter(software))
find_related(papers, RelatedThingGetter({**papers, **organisations}))
find_related(videos, RelatedThingGetter({**people, **papers, **software, **organisations}))
find_related(organisations, RelatedThingGetter({**people, **papers, **software}))

# Generate wordclouds
make_wordclouds(people, papers)

# Add members to global environment for navigation bar
make_members_global_for_navigation(people)

# Write all the people pages
write_people(people)
write_papers(papers)
write_categories(categories)
write_software(software)
write_videos(videos)
write_organisations(organisations)
write_pages(nav, people, papers, software, categories, videos, organisations)

# Copy static files to docs directory
os.system(r'copy files\* docs >nul')

# Save cache before finishing
save_cache()

# Check links
print('Finished generating HTML, now checking links.')
check_links()

# And we're done
print('Finished.')
