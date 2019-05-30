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
from storage import cache

def text_recognition(img):
    print('[info] initiating text recognition')
    start = time()
    texts = recognize_text(img)
    for text in texts:
        if len(text) > 1:
            s, p_cat, p_lvl = sentence_check(str(text))
            if p_cat[0] == 1:
                print(s + " = " + str(p_cat) + " | " + str(p_lvl))
    # print('text recognition is finished, current threads : {}'.format(active_count()))
    print('[info] text recognition done in {:.3f} seconds, there are now {} threads'.format(time()-start, active_count()))


if __name__ == '__main__':
    print('[info] system initiated')
    fnStart = time()
    cv2.destroyAllWindows()
    old_frame = grab()
    threads = []
    count = 0
    while(True):
        start = time()
        count += 1
        # print('start {}'.format(count))
        new_frame = grab() # averages around 0.1 seconds for each screenshot
        cache(new_frame, int(start))
        # extract range of interests from the background
        bg_roi = background_changes(new_frame, old_frame)

        threads = []
        for img in bg_roi:
            while (active_count() > 5):
                print('waiting for threads to reduce')
                sleep(0.1)
            t = Thread(target=text_recognition, args=(img,))
            t.start()
        
        for t in threads:
            t.join()
        
        # set the old frame
        old_frame = new_frame
        end = time()
        if ((end-start) < 1.5):
            sleep(1.5-(end-start))
        print('[info] time elapsed: {:.3f}'.format(end - start))

