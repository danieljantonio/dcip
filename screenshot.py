from mss import mss
import numpy as np
import cv2

def grab():
    with mss() as sct:
        # grab monitor size data
        monitor = sct.monitors[0]
        
        # grab the pixel data from the monitor as store it as an image
        sct_img = sct.grab(monitor)

        # convert the image into an numpy array so its compatible with opencv
        sct_img = np.array(sct_img)

        # return the BGR layers of the image
        return sct_img[:,:,:3]