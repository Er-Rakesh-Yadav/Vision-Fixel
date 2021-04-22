import cv2
import numpy as np
from kivy.app import App
from kivy.uix.image import Image
from PIL import Image, ImageFilter, ImageEnhance
from kivymd.toast import toast


class imgEnhanceColor():
    def __init__(self):
        pass
    def process(self,file):
        print("opearation applied")
        filename = file
        image = Image.open(filename)
        # size = width, height = image.size

        enhancer = ImageEnhance.Color(image)
        # if we give 0.0 then it will inhance in white and black
        image = enhancer.enhance(0.5)
        toast("operation applied")


        image.save('temp.png')
        print("opearation applied")

