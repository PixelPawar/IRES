import os


SEARCH_PATHS = [
    os.environ.get("PROGRAMFILES"),
    os.environ.get("PROGRAMFILES(X86)"),
    os.environ.get("LOCALAPPDATA"),
]


def find_executable(executable_name):
    """
    Search common Windows installation folders for an executable.
    """

    for base in SEARCH_PATHS:

        if not base:
            continue

        for root, dirs, files in os.walk(base):

            if executable_name in files:
                return os.path.join(root, executable_name)

    return None