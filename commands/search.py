import webbrowser
from speech import say


def google_search(search_query):
    """
    Pure executor.

    Performs a Google search using the supplied search text.
    """

    if not search_query:

        say("What would you like me to search for?")
        return True

    say(f"Searching Google for {search_query}")

    webbrowser.open(
        f"https://www.google.com/search?q={search_query}"
    )

    return True