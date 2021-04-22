import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from kivymd.toast import toast

class erosion():
    def __init__(self):
        pass
    def process(self,file):
        input_image = cv2.imread(file, cv2.IMREAD_COLOR)
        kernel = np.ones((5,5), np.uint8)
        erosion_image = cv2.erode(input_image, kernel, iterations=1)

        cv2.imwrite('temp.png', erosion_image)
        toast("Operation Applied")

        print("Operation Applied")


