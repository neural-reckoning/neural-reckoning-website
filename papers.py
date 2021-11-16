import datetime
from pathlib import Path
import re

from things import Thing
from templater import apply_template


class Paper(Thing):
    def validate(self):
        self.year = str(self.year)
        if hasattr(self, 'last_updated'):
            d, m, y = list(map(int, self.last_updated.split('-')))
            self.last_updated = datetime.datetime(y, m, d)
        elif self.year!="Preprints":
            self.last_updated = datetime.datetime(int(self.year), 1, 1)
        self.generate_link_icons()
    
    def generate_link_icons(self):
        # generate icons for links in paper
        new_urls = []
        icons = {}
        for (name, url) in self.urls:
            if re.search(r'\bvideo\b', name, flags=re.IGNORECASE):
                name = '<i class="fa fa-video-camera"></i> '+name
                if 'video' not in icons: # only use the first video link
                    icons['video'] = f'''
                        <a href="{url}" target="_blank">
                            <i class="fa fa-video-camera"></i>
                        </a>
                        '''
            if re.search(r'\bpdf\b', name, flags=re.IGNORECASE):
                name = '<i class="fa fa-file-pdf-o"></i> '+name
                if 'pdf' not in icons or 'preprint' in name.lower(): # use first pdf link or preprint version
                    icons['pdf'] = f'''
                        <a href="{url}" target="_blank">
                            <i class="fa fa-file-pdf-o"></i>
                        </a>
                        '''
            if re.search(r'\b(twitter|tweeprint)\b', name, flags=re.IGNORECASE):
                name = '<i class="fa fa-twitter"></i> '+name
                if 'twitter' not in icons: # use first twitter link
                    icons['twitter'] = f'''
                        <a href="{url}" target="_blank">
                            <i class="fa fa-twitter"></i>
                        </a>
                        '''
            if re.search(r'\bhtml\b', name, flags=re.IGNORECASE):
                name = '<i class="fa fa-newspaper-o"></i> '+name
                if 'html' not in icons: # use first html link
                    icons['html'] = f'''
                        <a href="{url}" target="_blank">
                            <i class="fa fa-newspaper-o"></i>
                        </a>
                        '''
            new_urls.append((name, url))
        self.urls = new_urls
        self.icons_dict = icons
        self.icons = ''.join([icon_html for icon_type, icon_html in sorted(icons.items(), reverse=True)])


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
