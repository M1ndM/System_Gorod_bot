from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


Window.size = (430, 650)
Window.color = (1, 0, 0, 1)


class Root(BoxLayout):
    def btn(self):
        show_popup()
    def priem(self):
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
            speak('Здравствуйте, я чат-бот для сбора показаний ЖКХ')
            speak('Скажите показания в виде' + ' "' + 'холодная вода на кухне, количество' + '"')
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
                    if s >= 71:
                        print(i)
                        list_pokazania.append(pokaz)


        def writePokaz():
            for index in list_pokazania:
                f.write(index + '\n')
            f.close()

        while True:
            if len(list_pokazania) < 5:
                dialogue()
            else:
                speak('Вы сказали все показания, досвидания!')
                writePokaz()
                quit()


class P(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return Root()

def show_popup():
    show = P()
    popupWindow = Popup(title='Popup', content=show,
                        size_hint=(None, None), size=(400, 400))
    popupWindow.open()

if __name__ == '__main__':
    MyApp().run()
