import subprocess

from config import APPLICATIONS
from speech import say
from utils.app_finder import find_application
from utils.parser import fuzzy_match, is_open_command
from utils.app_finder import find_application


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

    # Step 1: Search configured applications

    all_aliases = []

    for app in APPLICATIONS.values():
        all_aliases.extend(app["aliases"])

    match = fuzzy_match(app_name, all_aliases)

    if match:

        for app in APPLICATIONS.values():

            if match in app["aliases"]:

                say(f"Opening {app['display']}")

                try:
                    path = find_application(app["command"].replace(".exe", ""))

                    if path:
                        subprocess.Popen(path)
                    else:
                        subprocess.Popen(app["command"])

                    return True

                except Exception as e:
                    say(f"Unable to open {app['display']}")
                    print(e)
                    return True

    # Step 2: Search indexed applications

    path = find_application(app_name)

    if path:

        say(f"Opening {app_name}")

        try:
            subprocess.Popen(path)
            return True

        except Exception as e:
            say("Unable to open the application.")
            print(e)
            return True

    # Step 3: Nothing found

    say(f"I couldn't find {app_name}.")
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