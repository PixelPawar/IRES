import subprocess

from config import APPLICATIONS
from speech import say
from utils.app_finder import find_executable
from utils.parser import fuzzy_match, is_open_command


OPEN_WORDS = [
    "open",
    "launch",
    "start"
]


def open_application(query):
    """
    Opens an application based on the user's query.
    """

    if not is_open_command(query, OPEN_WORDS):
        return False

    app_name = extract_app_name(query)

    all_aliases = []

    for app in APPLICATIONS.values():
        all_aliases.extend(app["aliases"])

    match = fuzzy_match(app_name, all_aliases)

    if not match:
        return False

    for app in APPLICATIONS.values():

        if match in app["aliases"]:

            say(f"Opening {app['display']}")

            try:
                path = find_executable(app["command"])

                if path:
                    subprocess.Popen(path)
                else:
                    subprocess.Popen(app["command"])

                return True

            except Exception as e:
                say(f"Unable to open {app['display']}")
                print(e)
                return True

    return False


def extract_app_name(query):
    """
    Removes command words and returns only the application name.
    """

    words_to_remove = [
        "open",
        "launch",
        "start",
        "run",
        "please",
        "can",
        "could",
        "you"
    ]

    query = query.lower()

    for word in words_to_remove:
        query = query.replace(word, "")

    return " ".join(query.split())