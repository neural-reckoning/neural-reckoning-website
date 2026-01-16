import codecs, os, re

from jinja2 import Environment, FileSystemLoader, select_autoescape

additional_urls = []

def scan_html_for_links(page, name):
    for url in re.findall(r'''href\s*=\s*["']\s*(http.*?)\s*["']''', page):
        additional_urls.append((url, name))
    return page


env = Environment(loader=FileSystemLoader(['templates', 'temp']),
                  trim_blocks=True,
                  lstrip_blocks=True,
                  extensions=['jinja2.ext.loopcontrols'],
                  )
env.globals.update(dict(os=os, hasattr=hasattr, isinstance=isinstance, str=str, int=int))


def apply_template(name, filename, keys=None, keys_from=None):
    if keys is None:
        keys = {}
    if keys_from is not None:
        for k, v in keys_from.__dict__.items():
            if not k.startswith('_'):
                keys[k] = v
    keys['filename'] = filename
    if 'socialcard' not in keys:
        keys['socialcard'] = {}
    if 'description' not in keys['socialcard']:
        keys['socialcard']['description'] = ""
    if 'image' not in keys['socialcard']:
        keys['socialcard']['image'] = "default-social-media-card.png"
    page = env.get_template(name).render(**keys)
    codecs.open(os.path.join('docs', filename), 'w', encoding='utf-8').write(scan_html_for_links(page, filename))


def update_template_globals(**d):
    env.globals.update(d)
