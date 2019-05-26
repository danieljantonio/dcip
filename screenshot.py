from mss import mss
import numpy as np
import cv2
from time import time

def grab():
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        sct_img = np.array(sct_img)
        return sct_img[:,:,:3]

def grabAll():
    with mss() as sct:
        monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        sct_img = np.array(sct_img)
        return sct_img[:,:,:3]

timelist = []
timelistAll = []
for i in range(100):
        start = time()
        img = grab()
        end = time()
        # print('screenshot took {:.3f} seconds'.format(end-start))
        timelist.append(end-start)
for i in range(100):
        start = time()
        img = grabAll()
        end = time()
        # print('screenshot took {:.3f} seconds'.format(end-start))
        timelistAll.append(end-start)

print('the time grab() took was {:.4f} seconds'.format(np.mean(timelist)))
print('the time grabAll() took was {:.4f} seconds'.format(np.mean(timelistAll)))