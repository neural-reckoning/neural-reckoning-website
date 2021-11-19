import os

from collections import defaultdict

from things import Thing
from templater import apply_template


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
            for cid in pub.category_ids:
                cat = categories[cid]
                cat.add_thing(pub)
        pub.category_objects = set([categories[catid] for catid in pub.category_ids])

    for k, v in list(category_detail_links.items()):
        # category_detail_links[category_id(k)] = v
        categories[category_id(k)].detail_link = v

    # Generate category graphs and HTML maps
    numpapers = defaultdict(int)
    category_graph = defaultdict(set)
    category_connections = defaultdict(int)
    for pub in things:
        if not hasattr(pub, 'categories'):
            continue
        for cat in pub.category_objects:
            category_graph[cat.key] = set([])
            numpapers[cat.key] += 1
            for cat2 in pub.category_objects:
                if cat2.key<cat.key:
                    category_connections[cat.key, cat2.key] += 1

    max_connections = max(category_connections.values())
    min_connections = min(category_connections.values())
    max_num_papers = max(numpapers.values())
    min_num_papers = min(numpapers.values())
    for catname, inclusions in list(category_inclusions.items()):
        tgt_id = category_id(catname)
        for inclusion in inclusions:
            src_id = category_id(inclusion)
            category_graph[src_id].add(tgt_id)
    # Generate hierarchical categories
    category_dot_lines = []
    category_colours = {}
    for cat_id in list(category_graph.keys()):
        cat_name = category_id_names[cat_id]
        col = 0.7-0.7*(numpapers[cat_id]-min_num_papers)/(1.0*(max_num_papers-min_num_papers))
        col = int(255.0*col)
        col = ('%.02X' % col)*3
        col = '#'+col
        category_colours[cat_id] = col
        category_dot_lines.append('{cat_id} [URL="publication_category_{cat_id}.html", label="{cat_name}", color="{col}", fontcolor="{col}", '
                                'shape=box];'.format(cat_id=cat_id, cat_name=cat_name, col=col))
    for src_id, target_ids in list(category_graph.items()):
        for tgt_id in target_ids:
            category_dot_lines.append('{src_id} -> {tgt_id} [color="{col}"];'.format(src_id=src_id, tgt_id=tgt_id,
                                                                                    col=category_colours[tgt_id]))
    category_dot = '''
    digraph categories_hierarchy {{
        rankdir = LR;
    {graphspec}
    }}
    '''.format(graphspec='\n'.join(category_dot_lines))
    if not os.path.exists('temp'):
        os.mkdir('temp')
    open('temp/categories_hierarchy.dot', 'w').write(category_dot)
    layout_algo = 'dot'
    if os.system('{algo} -Tsvg temp/categories_hierarchy.dot -o temp/categories_hierarchy.svg'.format(algo=layout_algo))==0:
        svg = open('temp/categories_hierarchy.svg', 'r').read()
        svg = svg.replace('<svg', '<svg class="img-fluid"')
        open('temp/categories_hierarchy.svg', 'w').write(svg)
    # Spontaneous category graph
    category_dot_lines = []
    for (cat_id_1, cat_id_2), nc in list(category_connections.items()):
        col = 0.9-0.9*(nc-min_connections)/(1.0*(max_connections-min_connections))
        col = int(255.0*col)
        col = ('%.02X' % col)*3
        col = '#'+col
        category_dot_lines.append(
            '    {cat_id_1} -- {cat_id_2} [len={edgelen}, color="{col}"]'.format(cat_id_1=cat_id_1, cat_id_2=cat_id_2, nc=nc,
                                                                                col=col, edgelen=1.0/(max_connections/2+nc)))
    for cat_id in list(category_graph.keys()):
        cat_name = category_id_names[cat_id]
        col = category_colours[cat_id]
        category_dot_lines.append(
            '    {cat_id} [URL="publication_category_{cat_id}.html", label="{cat_name}", color="{col}", fontcolor="{col}", shape=box];'.format(
                cat_id=cat_id, cat_name=cat_name, col=col))
    category_dot = '''
    graph categories_spontaneous {{
        overlap=scale; splines=true;
    {graphspec}
    }}
    '''.format(graphspec='\n'.join(category_dot_lines))
    category_dot.replace('<svg', '<svg class="img-fluid" ')
    open('temp/categories_spontaneous.dot', 'w').write(category_dot)
    layout_algo = 'neato'
    if os.system('{algo} -Tsvg temp/categories_spontaneous.dot -o temp/categories_spontaneous.svg'.format(algo=layout_algo))==0:
        svg = open('temp/categories_spontaneous.svg', 'r').read()
        svg = svg.replace('<svg', '<svg class="img-fluid"')
        open('temp/categories_spontaneous.svg', 'w').write(svg)
    else:
        print("Couldn't run categories spontaneous dot")

    return categories


def write_categories(categories):
    for key, cat in categories.items():
        parents = [categories[c] for c in sorted([category_id(name) for name in category_inclusions.get(cat.name, [])])]
        subcats = [categories[c] for c in sorted([category_id(name) for name in category_descendants.get(cat.name, [])])]
        filename = f'publication_category_{key}.html'
        apply_template('category.html', filename, keys_from=cat,
            keys=dict(subcats=subcats, parents=parents, categories=categories))
