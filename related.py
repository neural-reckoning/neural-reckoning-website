def make_name2person(people):
    # build a map from author name representations to Person objects
    name2person = {}
    for person in people.values():
        for name in [person.name]+person.author_names:
            name = name.strip().lower()
            name2person[name] = person
    return name2person


def find_thing_authors(people, things, attr='authors'):
    name2person = make_name2person(people)
    # scan through software and add all authors to paper, and all software to authors
    for thing in things.values():
        if hasattr(thing, 'authors'):
            pubauths = thing.authors
        elif hasattr(thing, 'team'):
            pubauths = thing.team
        else:
            continue
        if isinstance(pubauths, str):
            pubauths = [a.strip() for a in pubauths.split(',')]
        thing.author_objects = [name2person.get(auth.lower(), auth) for auth in pubauths]
        # create HTML representation of author list
        newpubauths = []
        for authname, author in zip(pubauths, thing.author_objects):
            if isinstance(author, str):
                newpubauths.append(author)
            else:
                newpubauths.append(f'<a href="{author.key}.html">{authname}</a>')
        thing.authors_list_text = pubauths
        thing.authors = ', '.join(newpubauths)
        if len(pubauths)<=6:
            thing.authors_short = thing.authors
            thing.authors_short_list_text = thing.authors_list_text
        else:
            thing.authors_short = pubauths[0]+', et al.'
            thing.authors_short_list_text = [pubauths[0], 'et al.']
        # add thing to all authors
        for author in thing.author_objects:
            if not isinstance(author, str):
                author.add_thing(thing)
        # add PhD thesis to authors
        if hasattr(thing, 'phd_thesis') and thing.phd_thesis:
            assert len(thing.author_objects)==1
            author = thing.author_objects[0]
            author.phd_thesis = thing


class RelatedSoftwareGetter:
    def __init__(self, software):
        self.software = software
    def __call__(self, thing):
        related = []
        if hasattr(thing, 'software'):
            for tgt_str in thing.software:
                related.append(self.software[tgt_str.lower()])
        return related


class RelatedThingGetter:
    def __init__(self, things):
        self.things = things
    def __call__(self, thing):
        related = []
        if hasattr(thing, 'related'):
            for tgt_str in thing.related:
                related.append(self.things[tgt_str.lower()])
        return related


def find_related(things, get_related_things):
    if isinstance(things, dict):
        things = things.values()
    for src in things:
        targets = get_related_things(src)
        for tgt in targets:
            src.add_thing(tgt)
            tgt.add_thing(src)
