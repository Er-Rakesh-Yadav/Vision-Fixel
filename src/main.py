from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Mainwindow(BoxLayout):
    pass

class uiApp(App):

    def build(self):

        return Mainwindow()



if __name__ == "__main__":
    uiApp().run()