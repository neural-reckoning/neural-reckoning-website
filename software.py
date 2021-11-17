from pathlib import Path

from things import Thing
from templater import apply_template


class Software(Thing):
    def validate(self):
        if not hasattr(self, 'urls'):
            self.urls = []
        self.urls = [('Homepage', self.url)]+self.urls


def get_software():
    software = {}
    fnames = Path('software').rglob('*.yaml')
    for fname in fnames:
        sw = Software(fname)
        software[sw.key] = sw
    return software


def write_software(software):
    for key, sw in software.items():
        filename = f'sw_{key}.html'
        apply_template('single_software.html', filename, keys_from=sw)
