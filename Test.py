import speech_recognition as sr
import os
import pyttsx3


def talk(words):
    print(words)
    os.system('say ' + words)

talk("Привет спроси у нас что либо")


def command():
    r = sr.Recognizer

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("ничего не понял но очень интересно")
        zadanie = command()

        return zadanie
def makeSomething(zadanie):
    if "вода" in zadanie:
        talk("горячая")

while True:
    makeSomething(command())

