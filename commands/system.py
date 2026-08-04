import datetime
from speech import say


def tell_time(query):
    """
    Tell the current time.
    Returns True if the command was handled.
    """

    if "the time" in query or "time" in query:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        say(f"The time is {time_str}")
        return True

    return False


def exit_assistant(query):
    """
    Detect exit commands.
    Returns 'EXIT' if the assistant should stop.
    """

    if "stop" in query or "exit" in query:
        say("Have a nice day!")
        return "EXIT"

    return False