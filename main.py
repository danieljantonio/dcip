import cv2
from time import time, sleep
from screenshot import grab
from threading import Thread, active_count
import os
import numpy as np

from bg_changes import background_changes
from east import detect_text
from east_resize import resize32
from tesseract_ocr import recognize_text
from profanity import sentence_check

def text_recognition(img):
    texts = recognize_text(img)
    for text in texts:
        if len(text) > 1:
            s, p_cat, p_lvl = sentence_check(str(text))
            if p_cat[0] == 1:
                print(s + " = " + str(p_cat) + " | " + str(p_lvl))
    print('text recognition is finished, current threads : {}'.format(active_count()))


if __name__ == '__main__':
    fnStart = time()
    cv2.destroyAllWindows()
    old_frame = grab()
    threads = []
    count = 0
    while(True):
        start = time()
        count += 1
        print('start {}'.format(count))
        new_frame = grab() # averages around < 0.1 seconds for each screenshot

        # extract range of interests from the background
        bg_roi = background_changes(new_frame, old_frame)

        threads = []
        # print(len(bg_roi))
        for img in bg_roi:
            if (active_count() < 5):
                t = Thread(target=text_recognition, args=(img,))
                t.start()
                print('active threads: {}'.format(active_count()))
        
        for t in threads:
            t.join()
        
        # sleep(5)

        # set the old frame
        old_frame = new_frame
        end = time()
        if ((end-start) < 1.5):
            sleep(1.5-(end-start))
        # print('[info] time elapsed: {:.3f}'.format(time() - fnStart))


# img = cv2.imread('test_imgs/ss10.png', 1)
# text_recognition(img)