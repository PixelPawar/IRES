import os
import subprocess

from speech import say
from utils.paths import COMMON_FOLDERS


def open_folder(query):
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