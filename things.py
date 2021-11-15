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

        self.validate()


    def validate(self):
        pass