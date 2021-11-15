from collections import defaultdict

from things import Thing


category_inclusions = {
    'Brian': ['Neural simulation', 'Spiking'],
    'Neural simulation': ['Neuroinformatics', 'Spiking'],
    'Spike sorting': ['Neuroinformatics', 'Spiking', 'Neural data analysis'],
    'Neural data analysis': ['Neuroinformatics'],
    'Neuroinformatics': ['Neuroscience', 'Software'],
    'Sound localisation': ['Auditory', 'Neuroscience'],
    'Auditory': ['Sensory'],
    'Spiking': ['Neuroscience'],
    'Plasticity': ['Neuroscience'],
    'Learning': ['Neuroscience'],
    'Modelling': ['Neuroscience'],
    'Visual': ['Sensory'],
    'Virtual reality': ['Sensory']
    }

category_detail_links = {
    'Brian': 'software.html',
    'Neural simulation': 'neuroinformatics.html',
    'Spike sorting': 'software.html',
    'Neuroinformatics': 'neuroinformatics.html',
    'Sensory': 'sensory.html',
    'Software': 'software.html',
    }


class Category(Thing):
    def validate(self):
        self.things = defaultdict(list) # mapping self.things[classname] = list of things with that classname


def category_id(name):
    return name.lower().replace(' ', '')


def build_categories(things):
    things = [thing for thing in things.values() if hasattr(thing, 'categories')]
    categories = {}
    # generate inclusions and category ids for publications
    all_categories = set(list(category_inclusions.keys())+[cat for inc in list(category_inclusions.values()) for cat in inc])
    for pub in things:
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
        cat = Category(key=catid, name=name)
        categories[catid] = cat
        category_id_names[catid] = name
        category_id_inclusions[catid] = set([category_id(n) for n in recursive_inclusions(name)])

    for pub in things:
        names = pub.categories
        pub.category_ids = set([])
        for name in names:
            catid = category_id(name)
            category_id_names[catid] = name
            pub.category_ids.add(catid)
            if catid in category_id_inclusions:
                for cid in category_id_inclusions[catid]:
                    pub.category_ids.add(cid)
            cat = categories[catid]
            cat.things[pub.__class__.__name__].append(pub)
        pub.category_objects = set([categories[catid] for catid in pub.category_ids])

    for k, v in list(category_detail_links.items()):
        # category_detail_links[category_id(k)] = v
        categories[category_id(k)].detail_link = v

    return categories
