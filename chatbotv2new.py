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

    speak('Скажите показания')
    with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)
        pokaz = r.recognize_google(audio, language='ru')
        print(pokaz)
        for c in list_pokazania:
            b = fuzz.ratio(c, pokaz)
            if b > 80:
                speak('Вы уже говорили это')
        for i in opts["pokazania"]:
            s = fuzz.ratio(i, pokaz)
            if s >= 90:
                list_pokazania.append(pokaz)


def writePokaz():
    for index in list_pokazania:
        f.write(index + '\n')
    f.close()


speak('Здравствуйте, я чат-бот для сбора показаний ЖКХ')
while True:
    if len(list_pokazania) < 5:
        dialogue()
    else:
        speak('Вы сказали все показания, досвидания!')
        writePokaz()
        quit()