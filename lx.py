import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('Initializing LogicLinx')

MASTER = "Zyarexx"

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish user


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning" + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("How can I assist you today?")

# Function to take user command


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please...")
        query = None

    return query


# Main program
if __name__ == "__main__":
    print("Hello, my name is LogicLinx.")
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            # Add your music play logic here
            pass

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye!")
            break
