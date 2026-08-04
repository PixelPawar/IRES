import webbrowser
from speech import say

sites = {
    "youtube": "https://youtube.com",
    "wikipedia": "https://en.wikipedia.org",
    "google": "https://www.google.com"
}

def open_website(query):
    for name, url in sites.items():
        if f"open {name}" in query:
            say(f"Opening {name}")
            webbrowser.open(url)
            return True

    return False