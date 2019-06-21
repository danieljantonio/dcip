import cv2
from time import time, sleep, localtime, asctime
from screenshot import grab
from threading import Thread, active_count
import os
import numpy as np

from background_detection import background_changes
from storage import cache, clear_old_cache
from text_recognition import recognize_profanity

def get_maxthreads():
    # gets the maximum amount of threads allowed
    cpu = os.cpu_count()
    max_threads = (cpu * 2 * 2) + 2
    return max_threads

if __name__ == '__main__':
    print('[info] system initiated')
    print(asctime(localtime(time())))
    get_maxthreads()
    # fnStart = time()
    old_frame = grab()
    threads = []
    max_threads = get_maxthreads()
    while(True):
        clear_old_cache(120)
        start = time()
        filename = int(start) # stores the unix timestamp as filename 
        new_frame = grab() # screenshot the current frame
        cache(new_frame, filename) # saves current frame as an image with the timestamp as filename
        bg_roi = background_changes(new_frame, old_frame) # retrieving background difference from the current frame and previous frame

        threads = [] #creates a storage for the threads
        # for each of the area extracted by background changed, execute them individually in a threat
        for img in bg_roi:
            while (active_count() > max_threads):
                # sleep if the thread count exceeds thread limit
                sleep(0.1)
            # execute recognize_profanity in its own thread
            t = Thread(target=recognize_profanity, args=(img, filename,))
            t.start()
        
        # joins the threads stored
        for t in threads:
            t.join()
        
        # sets current frame as the old frame
        old_frame = new_frame 

        # limiter to ensure that the base time will be 1.5 seconds
        end = time()
        if ((end-start) < 1.5):
            sleep(1.5-(end-start))
        # print('[info] time elapsed: {:.3f}'.format(time() - start))

