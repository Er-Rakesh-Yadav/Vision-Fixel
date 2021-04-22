from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from PIL import Image
from kivy.uix.boxlayout import BoxLayout
import cv2
import numpy as np


Window.size = (400, 600)


class FirstScreen(Screen):
    pass


class SecondScreen(BoxLayout):
    img = ObjectProperty(None)


class FileLoader(BoxLayout):
    filechooser = ObjectProperty(None)


def navigation_draw():
    print("Navigation Is Working")


class mainApp(MDApp):
    def erosion(self):
        input_image = cv2.imread(self.img, cv2.IMREAD_COLOR)
        kernel = np.ones((5, 5), np.uint8)
        erosion_image = cv2.erode(input_image, kernel, iterations=1)
        erosion_image.save("temp.png")


    def dilate(self):
        input_image = cv2.imread(self.current_working_img, cv2.IMREAD_COLOR)
        kernel = np.ones((3, 3), np.uint8)
        dilation_image = cv2.dilate(input_image, kernel, iterations=1)
        cv2.imshow('dilation', dilation_image)

    def update(self, file):
        self.sec.img.source = file
        self.sec.img.reload()

    def load(self, path, filename):
        # print(path)
        # print(filename)
        self.update(filename[0])
        print(self.sec.img.source)
        self.screen.transition.direction = 'down'
        self.screen.current = 'secondscreen'

        self.current_working_img = filename[0]

    def save(self):
        im1 = Image.open(self.current_working_img)
        im1.save('temp.png')

    def mainscreen_to_fileloaderscreen(self):
        self.screen.transition.direction = 'up'
        self.screen.current = 'loaderscreen'

    def first_to_second(self):
        self.screen.transition.direction = 'left'
        self.screen.current = 'secondscreen'

    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'App/vision_icon.png'

        self.screen = ScreenManager()
        fir = FirstScreen()
        screen = Screen(name='firstscreen')
        screen.add_widget(fir)
        self.screen.add_widget(screen)

        self.sec = SecondScreen()
        screen = Screen(name='secondscreen')
        screen.add_widget(self.sec)
        self.screen.add_widget(screen)

        loader = FileLoader()
        screen = Screen(name='loaderscreen')
        screen.add_widget(loader)
        self.screen.add_widget(screen)
        # loadKv = Builder.load_string(kv)
        # screen.add_widget(loadKv)
        # print(screen.ids.img.source)
        return self.screen


mainApp().run()
