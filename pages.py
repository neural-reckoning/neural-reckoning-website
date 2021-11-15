import codecs, os

from templater import apply_template

def write_pages(nav, people, papers, software, categories):
    pages = nav['pages']
    unindexed_pages = nav['unindexed_pages']
    extra_keys = dict(
        publications=list(papers.values()),
        software=list(software.values()),
        members=list(people.values()),
    )

    # Generate index pages
    for filename, title in list(pages.items())+list(unindexed_pages.items()):
        extra_keys[title] = title
        extra_keys[filename] = filename
        apply_template(filename, filename, keys=extra_keys)
        print(filename)

