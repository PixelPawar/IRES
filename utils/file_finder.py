from difflib import get_close_matches

from utils.cache_manager import load_cache


def find_file(file_name, max_results=5):
    """
    Returns a list of matching files.
    """

    files = load_cache("files")

    if not files:
        return []

    file_name = file_name.lower()

    # Exact match
    if file_name in files:
        return [files[file_name]]

    matches = get_close_matches(
        file_name,
        files.keys(),
        n=max_results,
        cutoff=0.50
    )

    return [files[name] for name in matches]