import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from kivymd.toast import toast

class edgeDetection():
    def __init__(self):
        pass
    def process(self,file):
        input_image = cv2.imread(file, cv2.IMREAD_COLOR)
        kernel = np.ones((5,5), np.uint8)
        erosion_image = cv2.erode(input_image, kernel, iterations=1)
        e = input_image-erosion_image

        cv2.imwrite('temp.png', e)
        toast("Operation Applied")

        print("Operation Applied")
