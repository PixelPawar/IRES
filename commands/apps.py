import subprocess

from config import APPLICATIONS
from speech import say
from utils.app_finder import find_application
from utils.parser import fuzzy_match, is_open_command


OPEN_WORDS = [
    "open",
    "launch",
    "start",
]


def launch_application(app_name):
    """
    Pure executor.
    Launches an application using its display name or executable name.
    """

    # -----------------------------
    # Step 1: Configured applications
    # -----------------------------
    for app in APPLICATIONS.values():

        if (
            app_name.lower() == app["display"].lower()
            or app_name.lower() in [alias.lower() for alias in app["aliases"]]
        ):

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
                return False

    # -----------------------------
    # Step 2: Indexed applications
    # -----------------------------
    path = find_application(app_name)

    if path:

        say(f"Opening {app_name}")

        try:
            subprocess.Popen(path)
            return True

        except Exception as e:
            say("Unable to open the application.")
            print(e)
            return False

    # -----------------------------
    # Step 3: Not found
    # -----------------------------
    say(f"I couldn't find {app_name}.")
    return False


def open_application(query):
    """
    Temporary compatibility wrapper.

    This function exists so the current assistant keeps working
    while we migrate to the new NLP router.
    """

    if not is_open_command(query, OPEN_WORDS):
        return False

    app_name = extract_app_name(query)

    all_aliases = []

    for app in APPLICATIONS.values():
        all_aliases.extend(app["aliases"])

    match = fuzzy_match(app_name, all_aliases)

    if match:

        for app in APPLICATIONS.values():

            if match in app["aliases"]:
                return launch_application(app["display"])

    return launch_application(app_name)


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
        "you",
    ]

    query = query.lower()

    for word in words_to_remove:
        query = query.replace(word, "")

    return " ".join(query.split())