import cv2
import numpy as np
from kivy.app import App
from kivy.uix.image import Image
from PIL import Image, ImageFilter, ImageEnhance
from kivymd.toast import toast

class contrastAdjustment():
    def __init__(self):
        pass
    def process(self,file):
        img = cv2.imread(file)
        contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
        cv2.imwrite('temp.png', contrast_img)
        toast("operation applied")
        print("opearation applied")

