from pathlib import Path

from things import Thing
from templater import apply_template


class Paper(Thing):
    def validate(self):
        self.year = str(self.year)


def get_papers():
    papers = {}
    fnames = Path('papers').rglob('*.yaml')
    for fname in fnames:
        if 'paper_template' in str(fname):
            continue
        paper = Paper(fname)
        papers[paper.key] = paper
    return papers


def write_papers(papers):
    for key, paper in papers.items():
        filename = f'pub_{key}.html'
        apply_template('paper.html', filename, keys_from=paper)
