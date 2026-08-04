import json
import os

CACHE_FILE = "cache/apps.json"

SEARCH_PATHS = [
    os.environ.get("PROGRAMFILES"),
    os.environ.get("PROGRAMFILES(X86)"),
    os.environ.get("LOCALAPPDATA"),
]


def build_index():

    apps = {}

    for base in SEARCH_PATHS:

        if not base:
            continue

        for root, dirs, files in os.walk(base):

            for file in files:

                if file.endswith(".exe"):

                    name = file[:-4].lower()

                    if name not in apps:
                        apps[name] = os.path.join(root, file)

    with open(CACHE_FILE, "w") as f:
        json.dump(apps, f, indent=4)

    print(f"Indexed {len(apps)} applications.")