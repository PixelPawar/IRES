import json

CACHE_FILE = "cache/apps.json"


def load_index():

    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def find_application(name):

    apps = load_index()

    return apps.get(name.lower())