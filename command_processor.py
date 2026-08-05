from speech import say
from commands.files import open_file
from commands.browser import open_website
from commands.search import google_search
from commands.system import tell_time, exit_assistant
from commands.apps import open_application 
from commands.files import open_folder
from utils.logger import log

from ai import handle_ai_query

COMMANDS = [
    open_website,
    google_search,
    tell_time,
    open_folder,
    open_file,
    open_application,
    handle_ai_query,
]


def process_query(query):

    if not query:
        return

    if "hello" in query:
        say("Hello! How can I help you today.")
        return

    for command in COMMANDS:

        try:

            if command(query):
                return

        except Exception as e:

            log(f"{command.__name__}: {e}")

    say("Sorry, I don't understand that command.")