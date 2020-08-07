import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import sys
import subprocess
from pathlib import Path


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


engine = pyttsx3.init('nsss')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Jarvis. Please tell me how may i help you')

# It takes user input audio and converts into string


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Please wait, Calibrating Microphone')

        r.adjust_for_ambient_noise(source, duration=3)
        print('Listening.......')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query


if __name__ == "__main__":
    wishMe()
    if True:
        query = takeCommand().lower()

        # Execute the queries
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia...')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('firefox').open('https://www.youtube.com')
        elif 'open google' in query:
            webbrowser.get('firefox').open('https://www.google.com')
        elif 'open stackoverflow' in query:
            webbrowser.get('firefox').open('https://www.stackoverflow.com')

        elif 'play music' in query:
            webbrowser.get('firefox').open(
                'https://www.youtube.com/watch?v=A6topxBzFcs')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is, {strTime}')
        elif 'open code' in query:
            codePath = os.chdir('Applications/Visual\ Studio\ Code.app')
            open_file(codePath)
