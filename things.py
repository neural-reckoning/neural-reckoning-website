import os
import yaml

__all__ = ['Thing']

class Thing(object):
    short = ""
    long = ""
    icon = ""

    def __init__(self, fname):
        self._fname = fname
        _, tail = os.path.split(fname)
        self.key, _ = os.path.splitext(tail)
        self._yaml_obj = yaml.safe_load(open(fname, 'r'))
        for k, v in self._yaml_obj.items():
            setattr(self, k, v)
        self.validate()

    def validate(self):
        pass