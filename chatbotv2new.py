import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
speak_engine = pyttsx3.init()
r = sr.Recognizer()
opts = {
    "pokazania": ('холодная вода на кухне', 'горячая вода на кухне',
                  'горячая вода в туалете', 'холодная вода в туалете', 'электричество')
}
list_pokazania = []


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def dialogue():
    speak('tell me pokazania')
    f = open('list_pokazania.txt', 'w')
    with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)
        pokaz = r.recognize_google(audio, language='ru')
        if pokaz == opts["pokazania"]:
            if pokaz in list_pokazania:
                speak('you told it recently')
            else:
                print(pokaz)
                list_pokazania.append(pokaz)
                for index in list_pokazania:
                    f.write(index + '\n')
                print(list_pokazania)
                f.close()
        else:
            speak('we do not have this pokazanie')


while True:
    dialogue()
