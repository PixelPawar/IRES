import os
import subprocess

from speech import say
from utils.paths import COMMON_FOLDERS
from utils.file_finder import find_file


# =====================================================
# Pure Executors
# =====================================================

def launch_folder(folder_name):
    """
    Pure executor.

    Opens a common Windows folder.
    """

    if not folder_name:
        return False

    folder_name = folder_name.lower().strip()

    folder_path = COMMON_FOLDERS.get(folder_name)

    if not folder_path:
        return False

    if not folder_path.exists():
        say(f"{folder_name} folder was not found.")
        return False

    try:
        say(f"Opening {folder_name}")
        subprocess.Popen(f'explorer "{folder_path}"')
        return True

    except Exception as e:
        say("Unable to open the folder.")
        print(e)
        return False


def launch_file(file_name):
    """
    Pure executor.

    Opens a file from the indexed file database.
    """

    if not file_name:
        return False

    results = find_file(file_name)

    if not results:
        say(f"I couldn't find {file_name}.")
        return False

    # -----------------------------
    # Single match
    # -----------------------------
    if len(results) == 1:

        file = results[0]

        try:
            say(f"Opening {os.path.basename(file['path'])}")
            os.startfile(file["path"])
            return True

        except Exception as e:
            say("Unable to open the file.")
            print(e)
            return False

    # -----------------------------
    # Multiple matches
    # -----------------------------
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

        return False


# =====================================================
# Temporary Compatibility Wrappers
# =====================================================

def open_folder(query):
    """
    Temporary compatibility wrapper.
    Will be removed after the NLP migration.
    """

    query = query.lower()

    for folder_name in COMMON_FOLDERS:

        if folder_name in query:
            return launch_folder(folder_name)

    return False


def open_file(query):
    """
    Temporary compatibility wrapper.
    Will be removed after the NLP migration.
    """

    file_name = extract_file_name(query)

    return launch_file(file_name)


# =====================================================
# Helpers
# =====================================================

def extract_file_name(query):
    """
    Removes command words and returns only the file name.
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