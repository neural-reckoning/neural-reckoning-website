from collections import defaultdict
import codecs, os, datetime
import yaml

__all__ = ['Thing']

class Thing(object):
    short = ""
    long = ""
    icon = ""
    page_prefix = ""

    def __init__(self, fname=None, key=None, **kwds):
        if (fname is not None and key is not None) or (fname is None and key is None):
            raise ValueError("Provide one of fname or key")
        if fname is not None:
            self._fname = fname
            _, tail = os.path.split(fname)
            self.key, _ = os.path.splitext(tail)
            self._yaml_obj = yaml.safe_load(codecs.open(fname, 'r', encoding='utf-8'))
            for k, v in self._yaml_obj.items():
                setattr(self, k, v)
        else:
            self.key = key

        for k, v in kwds.items():
            setattr(self, k, v)

        self.things = defaultdict(set)

        if hasattr(self, 'last_updated'):
            d, m, y = list(map(int, self.last_updated.split('-')))
            self.last_updated = datetime.datetime(y, m, d)
            if not hasattr(self, 'year'):
                self.year = y

        if hasattr(self, 'name') and not hasattr(self, 'title'):
            self.title = self.name
        if hasattr(self, 'title') and not hasattr(self, 'name'):
            self.name = self.title

        self.page = f'{self.page_prefix}{self.key}.html'

        self.validate()

    def validate(self):
        pass

    def add_thing(self, thing):
        self.things[thing.__class__.__name__].add(thing)
        self.things['all'].add(thing)

    @property
    def paper_count(self):
        return len(self.things['Paper'])

    @property
    def software_count(self):
        return len(self.things['Software'])

    @property
    def thing_count(self):
        return len(self.things['all'])
