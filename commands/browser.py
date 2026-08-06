import webbrowser

from speech import say


SITES = {
    "youtube": "https://youtube.com",
    "wikipedia": "https://en.wikipedia.org",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt": "https://chat.openai.com",
}


def open_website(site_name):
    """
    Pure executor.

    Opens a website using its name.
    Returns True if successful, otherwise False.
    """

    if not site_name:
        return False

    site_name = site_name.lower().strip()

    if site_name in SITES:

        say(f"Opening {site_name}")

        webbrowser.open(SITES[site_name])

        return True

    say(f"I don't know the website {site_name}.")

    return False