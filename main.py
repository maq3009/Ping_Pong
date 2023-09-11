import kivy
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty


Window.size = (360, 800)

class LogInApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #self.manager = ScreenManager(transition = NoTransition())
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return self.manager
        
    def on_start(self):
        Clock.schedule_once(self.login, 7)
        
    def login(self, *args):
        self.manager.current = "login"


if __name__  == '__main__':
    LogInApp().run()
