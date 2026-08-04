import webbrowser
from speech import say


def google_search(query):
    """
    Search Google for the user's query.
    Returns True if the command was handled, otherwise False.
    """

    if "search for" in query:
        search_query = query.replace("search for", "").strip()

        if not search_query:
            say("What would you like me to search for?")
            return True

        say(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

        return True

    return False