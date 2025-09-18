import json

def generate_json_for_search(*thingsets):
    all_things = {}
    for thingset in thingsets:
        for name, thing in thingset.items():
            all_things[name] = thing._yaml_obj
    with open('docs/search_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_things, f, ensure_ascii=False, indent=2)