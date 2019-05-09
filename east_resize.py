import cv2
import numpy as np

def resize32(img, n):
    if (len(img.shape) == 3):
        (H,W) = img.shape[:2]
    else:
        (H,W) = img.shape
    h = int(H/n)
    w = int(W/n)
    if (h%32 != 0): 
        h = h + (32 - (h%32))
    if (w%32 != 0): 
        w = w + (32 - (w%32))
    return (h,w)