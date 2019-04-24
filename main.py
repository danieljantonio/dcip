from east import detect_text
from bg_changes import detect_changes
from east_resize import resize32, roi_resize32
from tesseract_ocr import recognize_texts
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import time


def main():
    first = True
    count = 0
    while(True):
        count += 1
        start = time.time()
        frame = ImageGrab.grab()
        frame_np = np.array(frame)
        frame = cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB)
        
        # Skip the first one
        if (first):
            frame_old = frame
            first = False
        
        # Get new h and w thats divisible by 32
        (new_h, new_w) = resize32(frame)

        # get the bg ROIs from the screenshot
        bg_roi = detect_changes(frame, frame_old, new_h, new_w)

        count2 = 0
        for bg_img in bg_roi:
            count2 += 1
            text_detection(bg_img, count, count2)
        
        # set current frame as the old frame before going to the next loop cycle
        frame_old = frame
        end = time.time()
        print("[INFO] text detection took {:.6f} seconds".format(end-start))


def text_detection(img, count, count2):
    print('text_detection')
    (H, W) = roi_resize32(img)
    (roi, img) = detect_text(img, 0.5, H, W, 0.5)
    texts = recognize_texts(roi)
    print(texts)
    cv2.imwrite(str(count) + "." + str(count2) + ".png", img)

main()