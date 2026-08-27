from pathlib import Path

from things import Thing
from templater import apply_template


class Talk(Thing):
    def validate(self):
        pass

def get_talks():
    talks = {}
    fnames = Path('talks').rglob('*.yaml')
    for fname in fnames:
        talk = Talk(fname)
        talks[talk.key] = talk
        talk.urls = [
            ('PPTX', f'https://raw.githubusercontent.com/neural-reckoning/slides/main/{talk.year}/{talk.key}.pptx'),
            ('PDF', f'https://raw.githubusercontent.com/neural-reckoning/slides/main/{talk.year}/{talk.key}.pdf'),
        ]
        talk.pdf_url = f'https://raw.githubusercontent.com/neural-reckoning/slides/main/{talk.year}/{talk.key}.pdf'
    return talks


def write_talks(talks):
    for key, talk in talks.items():
        filename = f'talk_{key}.html'
        apply_template('talk.html', filename, keys_from=talk)
