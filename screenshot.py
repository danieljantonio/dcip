from mss import mss
import numpy as np

def grab():
    with mss() as sct:
        monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        sct_img = np.array(sct_img)
        return sct_img[:,:,:3]