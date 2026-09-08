import codecs, os
from collections import defaultdict

from people import positions_in_order, position_headers
from templater import apply_template, update_template_globals


def make_members_global_for_navigation(people):
    members = list(people.values())
    grouped_members = defaultdict(list)
    for member in members:
        grouped_members[member.position].append(member)
    update_template_globals(members=members, grouped_members=grouped_members, positions_in_order=positions_in_order, position_headers=position_headers)


def write_pages(nav, people, papers, software, categories, videos, organisations, talks):
    all_things = {**people, **papers, **software, **videos, **organisations, **talks}.values()
    pages = nav['pages']
    unindexed_pages = nav['unindexed_pages']
    extra_keys = dict(
        publications=list(papers.values()),
        software=list(software.values()),
        videos=list(videos.values()),
        categories=categories,
        organisations=list(organisations.values()),
        talks=list(talks.values()),
        all_things=all_things,
    )

    # Generate index pages
    for filename, page_details in list(pages.items())+list(unindexed_pages.items())+list(nav['unlisted_pages'].items()):
        title = page_details['title']
        location = page_details['location']
        extra_keys['title'] = title
        extra_keys['filename'] = filename
        extra_keys['location'] = location
        apply_template(location, filename, keys=extra_keys)
