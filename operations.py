import cv2
import numpy as np

def get_kernel(shape,size):
    shapes={
        "Rectangle":cv2.MORPH_RECT,
        "Ellipse":cv2.MORPH_ELLIPSE,
        "Cross":cv2.MORPH_CROSS
    }
    return cv2.getStructuringElement(shapes[shape],(size,size))

def apply_operation(image, operation, kernel):
    ops = {
        "Erosion": lambda: cv2.erode(image, kernel),
        "Dilation": lambda: cv2.dilate(image, kernel),
        "Opening": lambda: cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel),
        "Closing": lambda: cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel),
        "Gradient": lambda: cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel),
        "Top Hat": lambda: cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel),
        "Black Hat": lambda: cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel),
    }
    return ops[operation]()