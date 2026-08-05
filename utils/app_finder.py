import json
import os
from difflib import get_close_matches

CACHE_FILE = "cache/apps.json"


def load_index():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r") as file:
        return json.load(file)


def find_application(app_name):
    """
    Search indexed applications using fuzzy matching.
    Returns the executable path or None.
    """

    applications = load_index()

    if not applications:
        return None

    # Exact match
    if app_name.lower() in applications:
        return applications[app_name.lower()]

    # Fuzzy match
    matches = get_close_matches(
        app_name.lower(),
        applications.keys(),
        n=1,
        cutoff=0.6
    )

    if matches:
        return applications[matches[0]]

    return None