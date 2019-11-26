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

        if query in lastpokazania:
            speak("ti sho peregrelsa")
            speak('ya ponyal chto ti terorist, zhdi fsb')
        else:
            if query in opts["tbr"]:
                speak('skoka, how much')
                with sr.Microphone(device_index=1) as source:
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language='ru-Ru')
                    print(query)
                    speak('dokazhi')
                    audio = r.listen(source)
                    query1 = r.recognize_google(audio, language='ru-RU')
                    print(query1)
                    if query1 == query:
                        lastpokazania.append(query1)
                        speak('ti proshol socialnii test, teper mi znaem chto ti ne terorist')
                    else:
                        speak('bipolarochka, obleisa holodnoy vodoy')
            else:
                speak("sam peregrelsa")
                speak('ya ponyal chto ti terorist, zhdi fsb')


while True:
    quest_answ()
