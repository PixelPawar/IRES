import webbrowser 

def google_search(query):
    if "search for" in query:
        search_query = query.replace("search for", "").strip()
        say(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

def exit_assistant():
    if "stop" in query or "exit" in query:
        say("Have a nice day")
        break