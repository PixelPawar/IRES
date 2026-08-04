from speech import say

from commands.browser import open_website
from commands.search import google_search
from commands.system import tell_time, exit_assistant

from ai import handle_ai_query


def process_query(query):

    if not query:
        return

    if "hello" in query:
        say("Hello! How can I help you today?")
        return

    if open_website(query):
        return

    if google_search(query):
        return

    if tell_time(query):
        return

    result = exit_assistant(query)
    if result == "EXIT":
        return "EXIT"

    # AI fallback
    handle_ai_query(query)