import pytesseract as pyt
import cv2
from time import time

def recognize(img):
    text = pyt.image_to_string(img)
    sentences = text.split("\n")
    texts = []
    for sentence in sentences:
        texts.append(sentence)
    return texts
