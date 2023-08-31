
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import kivy

kivy.require('2.2.1')

Window.size = (540, 960)

class LogInScreen(MDApp):
    def build(self):
        self.manager = ScreenManager(transition = NoTransition())
        self.manager.add_widget(Builder.load_file("pre-splash.kv"))
        return self.manager


if __name__ == "__main__":
    LogInScreen().run()


# from kivy.app import App
# from kivy.uix.label import Label


# class MyApp(App):
    
#     def build(self):
#         return Label(text = 'Hello World')
    
# if __name__  == '__main__':
#     MyApp().run()
