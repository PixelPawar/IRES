from difflib import get_close_matches
from utils.cache_manager import load_cache


def find_application(app_name):
    applications = load_cache("apps")

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
        cutoff=0.6,
    )

    if matches:
        return applications[matches[0]]

    return None