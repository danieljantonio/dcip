from east import recognize_text
from bg_changes import detect_changes
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import time

first = True
count = 0
while(True):
    frame = ImageGrab.grab()
    frame_np = np.array(frame)
    frame = cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB)
    
    if (first):
        first = False
        (H, W, D) = frame.shape
        frame_old = np.zeros((H, W, D), np.uint8)
    bg_roi = detect_changes(frame, frame_old)
    # text_roi = []
    # cv2.imshow('bg_roi', bg_roi)
    for bg_img in bg_roi:
        cv2.imshow('images test', bg_img)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    frame_old = frame
    # count += 1
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()