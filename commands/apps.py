from config import APPLICATIONS
from utils.parser import is_open_command
from speech import say
import subprocess
from utils.parser import fuzzy_match 
from utils.app_finder import find_executable


OPEN_WORDS = [
    "open",
    "launch",
    "start"
]


def open_application(query):

    if not is_open_command(query, OPEN_WORDS):
        return False

    for app in APPLICATIONS.values():

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



def extract_app_name(query):
    """
    Remove command words and return only the application name.
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