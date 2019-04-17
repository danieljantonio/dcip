from east import recognize_text
from bg_changes import detect_changes
from east_resize import resize32
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import time

first = True
count = 0
while(True):
    start = time.time()
    overallStart = time.time()
    frame = ImageGrab.grab()
    frame_np = np.array(frame)
    frame = cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB)
    end = time.time()
    print("[INFO] ImageGrab and conversion took {:.6f} seconds".format(end-start))
    
    # Skip the first one
    if (first):
        frame_old = frame
        first = False
    
    # Get new h and w thats divisible by 32
    (new_h, new_w) = resize32(frame)

    # get the bg ROIs from the screenshot
    start = time.time()
    bg_roi = detect_changes(frame, frame_old, new_h, new_w)
    end = time.time()
    print("[INFO] background detection took {:.6f} seconds".format(end-start))
    # bg_roi testing purposes
    # for bg_img in bg_roi:
    #     (H, W) = bg_img.shape[:2]
    #     bg_img = cv2.resize(bg_img, (int(W/3), int(H/3)))
    #     cv2.imshow('images test', bg_img)
    #     if cv2.waitKey(0) & 0xFF == ord('q'):
    #         break
    
    # set current frame as the old frame before going to the next loop cycle
    frame_old = frame
    end = time.time()
    print("[INFO] ImageGrab and background detection took {:.6f} seconds".format(end-overallStart))
    print()

cv2.destroyAllWindows()


start = time.time()
end = time.time()
print("[INFO] text detection took {:.6f} seconds".format(end-start))
