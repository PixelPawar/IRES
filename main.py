import speech_recognition as sr
import pyttsx3 
import webbrowser 
import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
import re

# Initialize engine ONCE
engine = pyttsx3.init()

# Tweak speech properties for better responsiveness
engine.setProperty('rate', 180)  # Speed of speech
engine.setProperty('volume', 1.0) 

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def say(txt):
    print(f"Assistant: {txt}")
    #Ensure engine doesn't hang
    if engine._inLoop:
        engine.endLoop()
    engine.say(txt)
    engine.runAndWait()

def take_task():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        r.pause_threshold = 0.6 # Wait 1 sec before considering a phrase finished
        print("Listening...")
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5) 
            audio_txt = r.recognize_google(audio, language="en-in")
            print("You said:", audio_txt)
            return audio_txt.lower() 
        except Exception as e:
            return ""

def ai_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {e}"

def save_filename(query, max_length=20): 
    filename = re.sub(r'[^\w\s-]', '', query)
    filename = filename.strip().replace(" ", '_')
    filename = filename[:max_length]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f'{filename}_{timestamp}.txt'

def save_response(query, response):
    os.makedirs("ai_responses", exist_ok=True)
    filename = save_filename(query)
    filepath = os.path.join("ai_responses", filename)
    with open(filepath, 'w', encoding="utf-8") as f:
        f.write(f'USER QUERY:\n{query}\n\nAI RESPONSE:\n{response}')
    print(f'Saved AI response to {filepath}')

def chat_with_me():
    # comming soon
    pass

if __name__ == '__main__':
    say("Assistant activated.")
    
    while True:
        query = take_task()
        if not query:
            continue

        #Simple Greeting
        elif "hello" in query:
            say("Hello! How can I help you today?")

        #Open Websites
        sites = [['youtube','https://youtube.com'],['wikipedia','https://en.wikipedia.org'],['google','https://www.google.com']]
        site_opened = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                site_opened = True
                break
        if site_opened: continue
        #Time
        if "the time" in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {time_str}")

        #Search
        elif "search for" in query:
            search_query = query.replace("search for", "").strip()
            say(f"Searching Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        #AI Response
        elif "using ai" in query:
            say("Consulting the AI, please wait...")
            response = ai_response(query)
            save_response(query, response)
            say("The answer has been saved to your folder.")

        #Exit Commands
        elif "stop" in query or "exit" in query:
            say("Have a nice day")
            break

        # just chatting
        elif "chat" in query:
            chat_response = chat_with_me()

        