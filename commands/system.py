import datetime

def tell_time():
    if "the time" in query:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        say(f"The time is {time_str}")