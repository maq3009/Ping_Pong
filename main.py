import kivy
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDAPP
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty




from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    
    def build(self):
        return Label(text = 'Hello World')
    
if __name__  == '__main__':
    MyApp().run()
