import speech_recognition as sr
import pyttsx3 


# Initialize engine ONCE
engine = pyttsx3.init()

# Tweak speech properties for better responsiveness
engine.setProperty('rate', 180)  # Speed of speech
engine.setProperty('volume', 1.0)



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
