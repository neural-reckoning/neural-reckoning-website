import codecs, glob, os

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


class Person(Thing):
    def validate(self):
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


def get_people():
    people = {}
    fnames = glob.glob('people/*.yaml')
    for fname in fnames:
        person = Person(fname)
        people[person.key] = person
    return people


def write_people(people):
    for key, person in people.items():
        filename = f'{key}.html'
        apply_template('person.html', filename, keys_from=person)
