import speech_recognition as sr
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
opts = {
     'alias': ("бот",'город бот','система город',
               'бот город','система город бот',"город"),
     "tbr":("скажи", "расскажи"),
     "cmds":{"wcounter":("я хочу дать показания по воде","вода","горячая вода"),
            "elcounter":("Электричество")}
 }

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
#функции
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаемся
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC
#Команды
def execute_cmd(cmd):
    if cmd == 'wcounter':
        print("Скажите что нибудь ...")

    with sr.Microphone(device_index=1) as source:
        audio2 = r.listen(source)
    query2 = r.recognize_google(audio2, language='ru-Ru')
    print(query2)


#запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

speak("Добрый день")
speak("Что вы хотели?")

stop_listening  = r.listen_in_background(m, callback)
while True: time.sleep(0.1)