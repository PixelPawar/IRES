import json
from pathlib import Path


CACHE_DIR = Path("cache")


def ensure_cache_dir():
    """
    Create the cache directory if it does not exist.
    """
    CACHE_DIR.mkdir(exist_ok=True)


def get_cache_path(cache_name):
    """
    Returns the path to a cache file.
    """
    ensure_cache_dir()
    return CACHE_DIR / f"{cache_name}.json"


def load_cache(cache_name):
    """
    Load JSON data from a cache file.
    Returns an empty dictionary if the file does not exist.
    """

    cache_path = get_cache_path(cache_name)

    if not cache_path.exists():
        return {}

    try:
        with open(cache_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_cache(cache_name, data):
    """
    Save JSON data to a cache file.
    """

    cache_path = get_cache_path(cache_name)

    with open(cache_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)