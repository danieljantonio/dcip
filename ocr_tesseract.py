import pytesseract as pyt
import cv2
from time import time

def recognize(img):
    # using pytesseract to generate string from the image
    text = pyt.image_to_string(img)

    # split the images 
    sentences = text.split("\n")

    # initializing an empty array to store the sentences
    texts = []

    # checking the sentences, removing those that has a length of less than 1
    for sentence in sentences:
        if len(sentence) > 1:
            texts.append(sentence)
    return texts
