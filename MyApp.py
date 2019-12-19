from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import speech_recognition as sr
import pyttsx3
from kivy.uix.button import Button
from kivy.uix.label import Label



Window.size = (430, 650)
Window.color = (1,0,0,1)

class Root(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()