import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
speak_engine = pyttsx3.init()
r = sr.Recognizer()
opts = {
    "alias": ('у меня есть', 'максим', 'макс', 'бот', 'внучек', 'внучёк', 'иношопотянин'),
    "tbr": ('вода', 'водичка', 'электричество'),
    "pokazania": ('туалет', 'в туалете', 'в санузле', 'на кухне', 'в кухне', 'санузел',
                       'кухня', 'ванная'),
    "lastpokazania": ('электричество', 'вода в ванной', 'вода на кухне'),

}


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def quest_answ(speak):
    with sr.Microphone(device_index=1) as source:
        speak(quest_answ(speak))
        audio = r.listen(source)
        query = r.recognize_google(audio, language='ru-RU')
        print(query)
        if audio == "tbr" + "pokazania" or "tbr":
            speak('скока, хау мач')
            with sr.Microphone(device_index=1) as source:
                audio = r.listen(source)
                query = r.recognize_google(audio, language='ru-RU')
                print(query)




while True:
    quest_answ(speak('skazhite pokazania'))