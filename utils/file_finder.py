from difflib import get_close_matches
import os

from utils.cache_manager import load_cache


def find_file(file_name, max_results=5):
    """
    Returns a list of matching files.
    Each result is a dictionary:
    {
        "name": filename,
        "path": full_path
    }
    """

    files = load_cache("files")

    if not files:
        return []

    file_name = file_name.lower()

    # Exact match
    if file_name in files:
        return [{
            "name": file_name,
            "path": files[file_name]
        }]

    matches = get_close_matches(
        file_name,
        files.keys(),
        n=max_results,
        cutoff=0.50
    )

    results = []

    for name in matches:
        results.append({
            "name": name,
            "path": files[name]
        })

    return results