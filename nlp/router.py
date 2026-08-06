from speech import say

from nlp.intents import Intent

from commands.apps import launch_application
from commands.search import google_search
from commands.system import tell_time
from commands.browser import open_website
from commands.files import launch_file, launch_folder

def _handle_greeting(_):
    say("Hello! How can I help you today?")
    return True


ROUTES = {
    Intent.OPEN_APPLICATION: lambda result: launch_application(
        result.entities["value"]
    ),

    Intent.SEARCH_GOOGLE: lambda result: google_search(
        result.entities["query"]
    ),

    Intent.ASK_TIME: lambda result: tell_time(),

    Intent.GREETING: _handle_greeting,

    # These will be enabled after we refactor commands/files.py
    #
    # Intent.OPEN_FOLDER: lambda result: launch_folder(
    #     result.entities["value"]
    # ),
    #
    # Intent.OPEN_FILE: lambda result: launch_file(
    #ROUTES = {
    Intent.OPEN_APPLICATION: lambda result: launch_application(
        result.entities["value"]
    ),

    Intent.OPEN_FOLDER: lambda result: launch_folder(
        result.entities["value"]
    ),

    Intent.OPEN_FILE: lambda result: launch_file(
        result.entities["value"]
    ),

    Intent.OPEN_WEBSITE: lambda result: open_website(
        result.entities["value"]
    ),

    Intent.SEARCH_GOOGLE: lambda result: google_search(
        result.entities["query"]
    ),

    Intent.ASK_TIME: lambda result: tell_time(),

    Intent.GREETING: _handle_greeting,
}




def route(result):
    """
    Routes an IntentResult to the appropriate executor.

    Returns:
        True  -> Intent handled
        False -> No matching route
    """

    handler = ROUTES.get(result.intent)

    if not handler:
        return False

    try:
        return handler(result)

    except Exception as e:
        print(f"[Router Error] {e}")
        return False