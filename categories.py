from collections import defaultdict

from things import Thing
from templater import apply_template

from matplotlib import cm, colors


category_inclusions = {
    'Brian': ['Neural simulation', 'Spiking', 'Neuromorphic'],
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
    'Virtual reality': ['Sensory'],
    'Multimodal': ['Sensory'],
    }

category_detail_links = {
    'Brian': 'software.html',
    'Neural simulation': 'neuroinformatics.html',
    'Spike sorting': 'software.html',
    'Neuroinformatics': 'neuroinformatics.html',
    'Sensory': 'sensory.html',
    'Software': 'software.html',
    'Metascience': 'metascience.html',
    }

category_descendants = defaultdict(set)
for descendant, parents in category_inclusions.items():
    for parent in parents:
        category_descendants[parent].add(descendant)


class Category(Thing):
    page_prefix = "publication_category_"


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

    for name in sorted(all_categories):
        catid = category_id(name)
        cat = Category(key=catid, name=name)
        categories[catid] = cat
        category_id_names[catid] = name
        category_id_inclusions[catid] = set([category_id(n) for n in recursive_inclusions(name)])

    for pub in things:
        names = pub.categories
        pub.category_ids = set([])
        for name in sorted(names):
            catid = category_id(name)
            category_id_names[catid] = name
            pub.category_ids.add(catid)
            if catid in category_id_inclusions:
                for cid in sorted(category_id_inclusions[catid]):
                    pub.category_ids.add(cid)
            for cid in sorted(pub.category_ids):
                cat = categories[cid]
                cat.add_thing(pub)
        pub.category_objects = set([categories[catid] for catid in pub.category_ids])

    for k, v in list(category_detail_links.items()):
        categories[category_id(k)].detail_link = v

    # Generate category graphs and HTML maps
    numpapers = defaultdict(int)
    category_graph = defaultdict(set)
    for pub in things:
        if not hasattr(pub, 'categories'):
            continue
        for cat in pub.category_objects:
            category_graph[cat.key] = set([])
            numpapers[cat.key] += 1

    for catname, inclusions in list(category_inclusions.items()):
        tgt_id = category_id(catname)
        for inclusion in sorted(inclusions):
            src_id = category_id(inclusion)
            category_graph[src_id].add(tgt_id)

    # Generate mermaid code
    generate_mermaid(category_graph, numpapers, category_id_names)

    return categories


def write_categories(categories):
    for key, cat in categories.items():
        parents = [categories[c] for c in sorted([category_id(name) for name in category_inclusions.get(cat.name, [])])]
        subcats = [categories[c] for c in sorted([category_id(name) for name in category_descendants.get(cat.name, [])])]
        filename = f'publication_category_{key}.html'
        apply_template('category.html', filename, keys_from=cat,
            keys=dict(subcats=subcats, parents=parents, categories=categories))


def generate_mermaid(category_graph, numpapers, category_id_names):
    max_num_papers = max(numpapers.values())
    min_num_papers = min(numpapers.values())
    category_colours = {}
    for cat_id in sorted(list(category_graph.keys())):
        col = (numpapers[cat_id]-min_num_papers)/(1.0*(max_num_papers-min_num_papers))
        col = cm.YlGn(0.1+0.6*col)
        col = colors.to_hex(col)#+'ee' # last bit is alpha
        category_colours[cat_id] = col

    lines = [
        "---",
        "config:",
        "   layout: elk",
        "---",
        "graph LR",
        ]  # LR = left-to-right
    
    for cat_id in sorted(category_colours.keys()):
        col = category_colours[cat_id]
        name = category_id_names[cat_id]
        lines.append(f'    {cat_id}[{name}]')
        lines.append(f'    style {cat_id} fill:{col},stroke:{col}')
        lines.append(f'    click {cat_id} "publication_category_{cat_id}.html" "Open category {name}"')

    for src, targets in sorted(category_graph.items()):
        if not targets:
            # ensure isolated nodes appear
            lines.append(f'    {src}')
            continue

        for dst in targets:
            lines.append(f'    {src} --> {dst}')

    open('temp/categories_hierarchy.mermaid', 'w').write('\n'.join(lines))
