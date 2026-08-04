import webbrowser 

def process_query(query):
        
    if not query:
        continue

    #Simple Greeting
    elif "hello" in query:
        say("Hello! How can I help you today?")

    #Open Websites

    site_opened = False
    for name, url in sites.items():
        if f"open {name}" in query:
            say(f"Opening {name}")
            webbrowser.open(url)
    if site_opened: continue

    #Time


    #Search


    #AI Response
    elif "using ai" in query:
        say("Consulting the AI, please wait...")
        response = ai_response(query)
        save_response(query, response)
        say("The answer has been saved to your folder.")

    #Exit Commands


    # just chatting
    elif "chat" in query:
        chat_response = chat_with_me()
