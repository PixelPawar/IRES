from nlp.intents import Intent

from commands.apps import open_application
from commands.browser import open_website
from commands.files import open_file, open_folder
from commands.search import google_search
from commands.system import tell_time
from ai import handle_ai_query
from speech import say


def route(result):
    """
    Execute the appropriate command based on the detected intent.
    """

    if result.intent == Intent.GREETING:
        say("Hello! How can I help you today?")
        return True

    if result.intent == Intent.OPEN_APPLICATION:
        return open_application(result.original_query)

    if result.intent == Intent.OPEN_FILE:
        return open_file(result.original_query)

    if result.intent == Intent.OPEN_FOLDER:
        return open_folder(result.original_query)

    if result.intent == Intent.SEARCH_GOOGLE:
        return google_search(result.original_query)

    if result.intent == Intent.ASK_TIME:
        return tell_time(result.original_query)

    if result.intent == Intent.AI_QUERY:
        return handle_ai_query(result.original_query)

    return False