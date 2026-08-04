import webbrowser 


sites = {
            'youtube':'https://youtube.com',
            'wikipedia':'https://en.wikipedia.org',
            'google':'https://www.google.com'
}


def open_website(query):
    site_opened = False
    for name, url in sites.items():
        if f"open {name}" in query:
            say(f"Opening {name}")
            webbrowser.open(url)
    if site_opened: continue