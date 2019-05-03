import cv2
import numpy as np

def resize32(img):
    if (len(img.shape) == 3):
        (H,W) = img.shape[:2]
    else:
        (H,W) = img.shape
    h = int(H/3)
    w = int(W/3)
    if (h%32 != 0): 
        h = h + (32 - (h%32))
    if (w%32 != 0): 
        w = w + (32 - (w%32))
    return (h,w)

def roi_resize32(img):
    if (len(img.shape) == 3):
        (H,W) = img.shape[:2]
    else:
        (H,W) = img.shape
    if (H%32 != 0): 
        H = H + (32 - (H%32))
    if (W%32 != 0): 
        W = W + (32 - (W%32))
    return (H,W)

def double_up(img):
    if (len(img.shape) == 3):
        (H,W) = img.shape[:2]
    else:
        (H,W) = img.shape
    return (H*2,W*2)