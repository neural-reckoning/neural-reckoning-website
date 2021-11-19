from pathlib import Path

from things import Thing
from templater import apply_template


class Organisation(Thing):
    page_prefix = "org_"
    def validate(self):
        if not hasattr(self, 'logo'):
            self.logo = 'default_org.png'

def get_organisations():
    organisations = {}
    fnames = Path('organisations').rglob('*.yaml')
    for fname in fnames:
        org = Organisation(fname)
        organisations[org.key] = org
    return organisations


def write_organisations(organisations):
    for key, org in organisations.items():
        filename = f'org_{key}.html'
        apply_template('organisation.html', filename, keys_from=org)
