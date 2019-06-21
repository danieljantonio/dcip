import cv2
from ocr_tesseract import recognize
from profanity import sentence_check
from time import time
from email_service import send_email
from threading import Thread



def recognize_profanity(img, filename):
    # print('[info] initiating text recognition')
    # start = time()

    # initialize an array to store the flagged sentences
    flags = []

    # get array of sentences from the tesseract OCR
    texts = recognize(img)

    # for each sentence in the array
    for text in texts:
        # check the array for its profanity level
        s, p_cat= sentence_check(str(text))

        # if the sentence is classified as profane (p_cat[0] == 1) 
        if p_cat[0] == 1:
            # append the text to the array of flags
            flags.append(s)
    
    # if there the array of flagged text is not empty
    if len(flags) > 0:
        # print('email sent')
        # send an email to
        send_email('djedidiaha@gmail.com', flags, filename)
    # print('[info] text recognition and profanity check done in {:.3f} seconds'.format(time()-start))
