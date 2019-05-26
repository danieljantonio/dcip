import pytesseract as pyt
import cv2
from time import time

def recognize_text(img):
    text = pyt.image_to_string(thresh)
    sentences = text.split("\n")
    texts = []
    for sentence in sentences:
        texts.append(sentence)
    return texts

def recognize_texts(imgs):
    texts = []
    for img in imgs:
        text = pyt.image_to_string(img) 
        texts.append(text)
    return texts