import os
import subprocess

from speech import say
from utils.paths import COMMON_FOLDERS
from utils.file_finder import find_file


def open_folder(query):
    """
    Opens common Windows folders.
    """
    query = query.lower()

    for folder_name, folder_path in COMMON_FOLDERS.items():

        if folder_name in query:

            if folder_path.exists():
                say(f"Opening {folder_name}")
                subprocess.Popen(f'explorer "{folder_path}"')
            else:
                say(f"{folder_name} folder was not found.")

            return True

    return False


def open_file(query):
    """
    Opens a file using the indexed file database.
    If multiple matches are found, the user is asked to choose one.
    """

    file_name = extract_file_name(query)

    results = find_file(file_name)

    if not results:
        return False

    # Only one match
    if len(results) == 1:

        file = results[0]

        try:
            say(f"Opening {os.path.basename(file['path'])}")
            os.startfile(file["path"])
            return True

        except Exception as e:
            say("Unable to open the file.")
            print(e)
            return True

    # Multiple matches
    say("I found multiple matching files.")

    print("\nMatching Files:\n")

    for i, file in enumerate(results, start=1):
        print(f"{i}. {os.path.basename(file['path'])}")

    say("Please type the number of the file you want to open.")

    choice = input("\nSelect file number: ")

    try:

        index = int(choice) - 1

        if index < 0 or index >= len(results):
            raise IndexError

        os.startfile(results[index]["path"])

        say("Opening file.")

        return True

    except (ValueError, IndexError):

        say("Invalid selection.")

        return True


def extract_file_name(query):
    """
    Remove command words and return only the file name.
    """

    words = [
        "open",
        "find",
        "show",
        "launch",
        "please",
    ]

    query = query.lower()

    for word in words:
        query = query.replace(word, "")

    return " ".join(query.split())