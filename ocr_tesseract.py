import pytesseract as pyt
import cv2
from time import time

def recognize(img):
    text = pyt.image_to_string(img)
    sentences = text.split("\n")
    # print(sentences)
    texts = []
    for sentence in sentences:
        if len(sentence) > 1:
            # print(sentence)
            texts.append(sentence)
    # print(texts)
    return texts

# img = cv2.imread('texet.png')
# recognize(img)