import cv2
from time import time, sleep, localtime, asctime
from screenshot import grab
from threading import Thread, active_count
import os
import numpy as np

from background_detection import background_changes
from resize import resize32
from storage import cache, clear_old_cache
from text_recognition import recognize_profanity

def get_maxthreads():
    cpu = os.cpu_count()
    max_threads = (cpu * 2 * 2) + 2
    return max_threads

if __name__ == '__main__':
    print('[info] system initiated')
    get_maxthreads()
    fnStart = time()
    cv2.destroyAllWindows()
    old_frame = grab()
    threads = []
    max_threads = get_maxthreads()
    count = 0
    hits = 0
    print(asctime(localtime(fnStart)))
    while(True):
        clear_old_cache(60)
        start = time()
        filename = int(start)
        count += 1
        new_frame = grab() 
        cache(new_frame, filename)
        bg_roi = background_changes(new_frame, old_frame)

        threads = []
        for img in bg_roi:
            while (active_count() > max_threads):
                print('waiting for threads to reduce')
                sleep(0.1)
                hits += 1
            t = Thread(target=recognize_profanity, args=(img, filename,))
            t.start()
        
        for t in threads:
            t.join()
        
        # set the old frame
        old_frame = new_frame
        end = time()
        # print(hits)
        if ((end-start) < 1.5):
            sleep(1.5-(end-start))
        # print('[info] time elapsed: {:.3f}'.format(end - start))

