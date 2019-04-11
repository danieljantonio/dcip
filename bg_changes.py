from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
import cv2
import numpy as np
from imutils import resize


def detect_changes(frame_prev, frame_curr, new_w=960, new_h=544):
    original_frame = frame_curr.copy()
    (frame_h, frame_w) = original_frame.shape[:2]
    ratio_h = frame_h / new_h
    ratio_w = frame_w / new_w

    frame1 = cv2.resize(frame_prev, (new_w, new_h))
    frame2 = cv2.resize(frame_curr, (new_w, new_h))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    frames = [frame1, frame2]

    rects = []
    roi = []
    
    fgmask = fgbg.apply(frame1)
    fgmask = fgbg.apply(frame2)

    kernel = np.ones((9,9), np.uint8)
    dilate = cv2.dilate(fgmask, kernel, iterations=2)

    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)

        start_x = int(x * ratio_w)
        start_y = int(y * ratio_h)
        end_x = int((x+w) * ratio_w)
        end_y = int((y+h) * ratio_h)

        roi.append(original_frame[start_y:end_y, start_x:end_x])
    return roi


# img1 = cv2.imread('east/img/frame1.png')
# img2 = cv2.imread('east/img/frame2.png')

# roi = detect_changes(img1, img2)

# for img in roi:
#     cv2.imshow('img', img)
#     cv2.waitKey(0)


# cv2.destroyAllWindows()
