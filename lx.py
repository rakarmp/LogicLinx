import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from gtts import gTTS
import playsound

print('Initializing LogicLinx')

MASTER = "Zyarexx"

# Function to speak


def speak(text):
    tts = gTTS(text=text, lang='id')
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

# Function to wish user


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Selamat pagi" + MASTER)
    elif 12 <= hour < 18:
        speak("Selamat siang" + MASTER)
    else:
        speak("Selamat malam" + MASTER)
    speak("Ada yang bisa saya bantu?")

# Function to take user command


def takeCommand():
    r = sr.Recognizer()
    # Use the appropriate device index
    microphone = sr.Microphone(device_index=0)

    with microphone as source:
        print("Mendengarkan...")
        audio = r.listen(source)

    try:
        print("Mengenali...")
        query = r.recognize_google(audio, language="id-ID")
        print(f"Pengguna berkata: {query}\n")

    except Exception as e:
        print("Tolong ulangi...")
        query = None

    return query


# Main program
if __name__ == "__main__":
    print("Halo, nama saya LogicLinx.")
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Mencari di Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'buka youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'buka google' in query:
            webbrowser.open("https://www.google.com")

        elif 'putar musik' in query:
            # Tambahkan logika untuk memutar musik di sini
            pass

        elif 'jam berapa' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Jam sekarang {strTime}")

        elif 'keluar' in query or 'tutup' in query:
            speak("Sampai jumpa!")
            break
