import cv2
import numpy as np
from PIL import Image


def load_image(upload_file):
    image=Image.open(upload_file).convert("RGB")
    return np.array(image)


def to_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

def generate_test_image():
    img=np.zeros((300,300),dtype=np.uint8)
    cv2.circle(img,(150,150),80,255,-1)
    cv2.rectangle(img,(50,50),(100,100),255,-1)
    return img