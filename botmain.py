import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
speak_engine = pyttsx3.init()
r = sr.Recognizer()
opts = {
    "alias": ('максим', 'макс', 'бот', 'внучек', 'внучёк', 'иношопотянин'),
    "tbr": ('вода', 'водичка', 'электричество'),
    "pokazania": ('туалет', 'в туалете', 'в санузле', 'на кухне', 'в кухне', 'санузел',
                       'кухня', 'ванная'),

}
lastpokazania = []


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def quest_answ():
    with sr.Microphone(device_index=1) as source:
        speak('skazhite pokazania')
        audio = r.listen(source)
        query = r.recognize_google(audio, language='ru-RU')
        print(query)
        lastpokazania.append(query)
    if query in opts["tbr"]:
        with sr.Microphone(device_index=1) as source:
            speak('скока, хау мач')
            audio = r.listen(source)
            query2 = r.recognize_google(audio, language='ru-RU')
            print(query2)
    else:
        speak("ty sho peregrelsa")


while True:
    quest_answ()
