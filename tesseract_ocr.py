import pytesseract as pyt

def recognize_text(img):
    text = pyt.image_to_string(img)
    return text

def recognize_texts(imgs):
    texts = []
    for img in imgs:
        text = pyt.image_to_string(img)
        texts.append(text)
    return texts