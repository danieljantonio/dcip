import cv2
from ocr_tesseract import recognize
from profanity import sentence_check
from time import time
from email_service import send_email
from split_image import split_image
from threading import Thread
from profanity_filter import filter

# def recognize_profanity(img, filename):
#     imgs = split_image(img)
#     threads = []
#     for im in imgs:
#         t = Thread(target=detect_profanity, args=(im, filename))
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()


def recognize_profanity(img, filename):
# def detect_profanity(img, filename):
    # print('[info] initiating text recognition')
    start = time()
    flags = []
    texts = recognize(img)
    for text in texts:
        s, p_cat= sentence_check(str(text))
        if p_cat[0] == 1:
            flags.append(s)
        # p_cat = filter(str(text))
        # if p_cat == 1:
        #     flags.append(text)
    if len(flags) > 0:
        # print('send mail')
        send_email('djedidiaha@gmail.com', 'Daniel Antonio', flags, filename)
    print('[info] text recognition and profanity check done in {:.3f} seconds'.format(time()-start))
