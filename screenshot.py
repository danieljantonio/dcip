from mss import mss
import numpy as np

def grab():
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        return np.array(sct_img)
