from config import APPLICATIONS, WEBSITES
from utils.paths import COMMON_FOLDERS
from utils.file_finder import find_file


def extract_application(query):
    """
    Extract an application name from the user's query.
    Returns the application's display name if found.
    """

    query = query.lower()

    for app in APPLICATIONS.values():

        for alias in app["aliases"]:

            if alias.lower() in query:
                return app["display"]

    return None


def extract_folder(query):
    """
    Extract a common folder name from the query.
    Returns the folder name if found.
    """

    query = query.lower()

    for folder in COMMON_FOLDERS.keys():

        if folder.lower() in query:
            return folder

    return None


def extract_website(query):
    """
    Extract a website from the query.
    Returns the website key if found.
    """

    query = query.lower()

    for website in WEBSITES.keys():

        if website.lower() in query:
            return website

    return None


def extract_file(query):
    """
    Extract a file from the indexed file database.
    Returns the filename if found.
    """

    query = query.lower()

    results = find_file(query)

    if not results:
        return None

    # find_file() returns a list of matches.
    # Return the filename of the best match.
    return results[0]["name"]