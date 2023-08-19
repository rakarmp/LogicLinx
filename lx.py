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

# function


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

# microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognation...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

# main program


speak("Hello my name is LogicLinx, how can I help you?")
wishMe()
query = takeCommand()

# logic for task as per query
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
