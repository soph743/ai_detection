from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    def btn(self):
        show_popup()


class ThirdWindow(Screen):
    def btn(self):
        show_popup()


class P(FloatLayout):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("AI_detection.kv")


class MyMainApp(App):
    def build(self):
        return kv


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    MyMainApp().run()
