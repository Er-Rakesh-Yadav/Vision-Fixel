from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class Mainwindow(MDBoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'vision_icon.png'
        return Mainwindow()


MainApp().run()
