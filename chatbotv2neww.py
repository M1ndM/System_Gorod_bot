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

f = open('list_pokazania.txt', 'w')


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def dialogue():
    speak('tell me pokazania')
    with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)
        pokaz = r.recognize_google(audio, language='ru')
        print(pokaz)
        if pokaz in opts["pokazania"]:
            if pokaz in list_pokazania:
                speak('you told it recently')
            else:
                list_pokazania.append(pokaz)
                print(list_pokazania)
        else:
            speak('we do not have this pokazanie')


while True:
    if len(list_pokazania) < 5:
        dialogue()
    else:
        speak('you told me all pokazania, goodbye!')
        for index in list_pokazania:
            f.write(index + '\n')
        f.close()
        quit()
