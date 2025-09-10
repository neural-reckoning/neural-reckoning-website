import codecs, glob, os
from collections import defaultdict

from PIL import Image, ImageDraw

from get_orcid_data import get_orcid_publications
from get_semantic_scholar_data import get_semantic_scholar_publications
from things import Thing
from email_addresses import generate_email
from templater import apply_template

__all__ = ['Person']

def sk_address(room):
    return '''
    Room {room}
    Department of Electrical and Electronic Engineering
    Imperial College
    Exhibition Road
    London SW7 2AZ
    '''.format(room=room)

positions_in_order = ['pi', 'postdoc', 'phd', 'other', 'affiliated','former']
position_order_map = dict(zip(positions_in_order, range(len(positions_in_order))))
position_headers = {
    'pi': '',
    'postdoc': 'Postdocs and Fellows',
    'phd': 'PhD students',
    'other': 'Others',
    'affiliated': 'Affiliated members',
    'former': 'Former members',
    }

relationship_types = {
    'mentor': ('Mentored by', 'Mentor to'),
    'supervisor': ('Supervised by', 'Supervises'),
    'collaborator': ('Works with', 'Works with'),
    }

class Person(Thing):
    def validate(self):
        if hasattr(self, 'positions'):
            earliest = min(p['start'] for p in self.positions)
            end_times = [p['end'] for p in self.positions if 'end' in p]
            if len(end_times)==len(self.positions):
                latest = max(end_times)
                self.lab_member_dates = [earliest, latest]
            else:
                self.lab_member_dates = [earliest]
            if not hasattr(self, 'dates'):
                self.dates = self.lab_member_dates
            if 'end' in self.positions[0]:
                current_position = 'former'
            else:
                current_position = self.current_position = self.positions[0]
                self.position = current_position['type']
                if 'relationships' in current_position:
                    self.relationships = current_position['relationships']
        self.papers = []
        if not hasattr(self, 'address'):
            if hasattr(self, 'room'):
                self.address = sk_address(self.room)
            else:
                self.address = ''
        if hasattr(self, 'email'):
            self.email_img = generate_email(self.key, self.email)
        if hasattr(self, 'dates'):
            if len(self.dates)==1:
                self.dates_string = str(self.dates[0])+'-'
            else:
                self.dates_string = '-'.join(map(str, self.dates))
        if not hasattr(self, 'show_publications'):
            self.show_publications = True
        if not hasattr(self, 'external_publications'):
            self.external_publications = False
        self.position_order = position_order_map[self.position.lower()]
        # "logo" used for display
        self.logo = f"photo_{self.key}.s.circ.png"
        # load external publications if desired
        if hasattr(self, 'orcid'):
            self.external_publications = get_orcid_publications(self.orcid)
        elif hasattr(self, 'semantic_scholar'):
            self.external_publications = get_semantic_scholar_publications(self.semantic_scholar)

def get_people():
    people = {}
    fnames = glob.glob('people/*.yaml')
    for fname in fnames:
        person = Person(fname)
        people[person.key] = person
        if not hasattr(person, 'relationships'):
            person.relationships = {}
        person.formatted_relationships = defaultdict(list)
    for person in people.values():
        for relationship_type, target_keys in person.relationships.items():
            rel_forward, rel_backward = relationship_types[relationship_type]
            person.formatted_relationships[rel_forward] = [people[target_key] for target_key in target_keys]
            for target_key in target_keys:
                target = people[target_key]
                target.formatted_relationships[rel_backward].append(person)
    return people


def write_people(people):
    for key, person in people.items():
        filename = f'{key}.html'
        apply_template('person.html', filename, keys=dict(person=person), keys_from=person)


def make_people_thumbnails(people):
    medium = 100
    small = 75
    def add_transparent_circle(im):
        w, h = im.size
        mask = Image.new("L", (w*5, h*5), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, w*5, h*5), fill=255)
        mask = mask.resize((w, h))
        im.putalpha(mask)
    photo_fnames = [
        #('files/portrait_placeholder', '.png')
        ]
    for member in people.values():
        photo_fnames.append(('files/photo_'+member.key, '.jpg'))
    for base, ext in photo_fnames:
        if os.path.exists(base+ext):
            try:
                with Image.open(base+ext) as im:
                    # medium size thumbnail is just square
                    im_medium = im.copy()
                    im_medium.thumbnail((medium, medium))
                    #im_medium.save(base+'.m.jpg')
                    add_transparent_circle(im_medium)
                    im_medium.save(base+'.m.circ.png')
                    # small thumbnail is circle
                    im_small = im.copy()
                    im_small.thumbnail((small, small))
                    #im_small.save(base+'.s.jpg')
                    add_transparent_circle(im_small)
                    im_small.save(base+'.s.circ.png')
            except OSError:
                print('Cannot create thumbnail for', base)