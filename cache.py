import os, json

__all__ = ['cached', 'save_cache']

if os.path.exists('cached.json'):
    cached = json.load(open('cached.json', 'r'))
else:
    cached = {}

def save_cache():
    json.dump(cached, open('cached.json', 'w'), sort_keys=True, indent=4)
    