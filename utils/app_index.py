import os

from utils.cache_manager import save_cache

SEARCH_PATHS = [
    os.environ.get("PROGRAMFILES"),
    os.environ.get("PROGRAMFILES(X86)"),
    os.environ.get("LOCALAPPDATA"),
]


def build_index():
    """
    Scan common installation folders and build an application index.
    """

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

    save_cache("apps", apps)

    print(f"Indexed {len(apps)} applications.")