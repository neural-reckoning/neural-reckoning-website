from collections import defaultdict
import codecs, os
import yaml

__all__ = ['Thing']

class Thing(object):
    short = ""
    long = ""
    icon = ""

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
