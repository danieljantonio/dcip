import cv2
import numpy as np

def resize_n(img, n):
    # getting the height and the width of the image
    if (len(img.shape) == 3):
        (H,W) = img.shape[:2]
    else:
        (H,W) = img.shape
    # returning the resized image based on the N value provided in the parameter
    return (int(H/n), int(W/n))