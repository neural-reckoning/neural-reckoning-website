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


def write_pages(nav, people, papers, software, categories, videos):
    pages = nav['pages']
    unindexed_pages = nav['unindexed_pages']
    extra_keys = dict(
        publications=list(papers.values()),
        software=list(software.values()),
        videos=list(videos.values()),
        categories=categories,
    )

    # Generate index pages
    for filename, title in list(pages.items())+list(unindexed_pages.items()):
        extra_keys[title] = title
        extra_keys[filename] = filename
        apply_template(filename, filename, keys=extra_keys)
