from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from PIL import Image
from kivy.uix.boxlayout import BoxLayout
import cv2

from App.src.Erosion import erosion
from App.src.EdgeDetection import edgeDetection
from ImgEnhanceColor import imgEnhanceColor
from App.src.ContrastAdjustment import contrastAdjustment

Window.size = (400, 600)


class FirstScreen(Screen):
    pass


class SecondScreen(BoxLayout):
    img = ObjectProperty(None)


class FileLoader(BoxLayout):
    filechooser = ObjectProperty(None)


class mainApp(MDApp):
    current_working_image = None
    current_operation_performed = None

    def imgEnhanceColorMethod(self):
        if mainApp.current_working_image is None:
            toast("select the image first")

        else:
            obj = imgEnhanceColor()
            obj.process('temp.png')
            self.update('temp.png')
            mainApp.current_operation_performed = 'EnhanceColor'

    def contrastAdjustmentMethod(self):
        if mainApp.current_working_image is None:
            toast("select the image first")

        else:
            obj = contrastAdjustment()
            obj.process('temp.png')
            self.update('temp.png')
            mainApp.current_operation_performed = 'ContrastAdjustment'

    def erosionMethod(self):
        if mainApp.current_working_image is None:
            toast("select the image first")

        else:
            obj = erosion()
            obj.process('temp.png')
            self.update('temp.png')
            mainApp.current_operation_performed = 'Erosion'

    def edgeDetectionMethod(self):

        if mainApp.current_working_image is None:
            toast("select the image first")

        else:
            obj = edgeDetection()
            obj.process('temp.png')
            self.update('temp.png')
            mainApp.current_operation_performed = 'EdgeDetection'

    def update(self, file):
        try:
            self.sec.img.source = file
            self.sec.img.reload()
        except:
            toast("OOPss!!!")

    def load(self, path, filename):

        self.update(filename[0])
        mainApp.current_working_image = filename[0]
        image = cv2.imread(filename[0])
        cv2.imwrite('temp.png', image)
        mainApp.current_operation_performed = None
        self.screen.transition.direction = 'down'
        self.screen.current = 'secondscreen'

    def reset(self):
        self.update(mainApp.current_working_image)

    def save(self):
        if mainApp.current_operation_performed is not None:
            im1 = Image.open('temp.png')
            im1.save(mainApp.current_operation_performed + '.png')
            toast('saved as ' + mainApp.current_operation_performed + ' .png')
            return 0
        im1 = Image.open('temp.png')
        im1.save('output.png')
        toast('saved as output.png')

    def mainscreen_to_fileloaderscreen(self):
        self.screen.transition.direction = 'up'
        self.screen.current = 'loaderscreen'

    def first_to_second(self):
        self.screen.transition.direction = 'right'
        self.screen.current = 'secondscreen'

    def build(self):
        self.current_working_img = '/home/rakesh/PycharmProjects/Vision-Fixel/App/img/img.png'
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'img/vision_icon.png'

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
        return self.screen


mainApp().run()
