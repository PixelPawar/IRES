import datetime
from speech import say


def tell_time(_=None):
    """
    Pure executor.

    Speaks the current time.
    """

    time_str = datetime.datetime.now().strftime("%I:%M %p")

    say(f"The time is {time_str}")

    return True


def exit_assistant(query):
    """
    Detect exit commands.
    Returns 'EXIT' if the assistant should stop.
    """

    if "stop" in query or "exit" in query:
        say("Have a nice day!")
        return "EXIT"

    return False