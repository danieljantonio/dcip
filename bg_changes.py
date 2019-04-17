from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
import cv2
import numpy as np
from imutils import resize


def detect_changes(frame_curr, frame_prev=0, new_h=544, new_w=960):
    if (type(frame_prev) == "<class 'numpy.ndarray'>"):
        frame_prev = np.array((1,1,3))
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
    closing = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

    contours,_ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print("Contours found = {}".format(len(contours)))
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        start_x = int(x * ratio_w)
        start_y = int(y * ratio_h)
        end_x = int((x+w) * ratio_w)
        end_y = int((y+h) * ratio_h)

        rects.append((start_x, start_y, end_x, end_y))
    
    boxes = non_max_suppression(np.array(rects))

    for (start_x, start_y, end_x, end_y) in boxes:
        cv2.rectangle(frame1, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        roi.append(original_frame[start_y:end_y, start_x:end_x])
    return roi


# img1 = cv2.imread('east/img/frame1.png')
# img2 = cv2.imread('east/img/frame2.png')

# roi = detect_changes(img2, img1)

# for img in roi:
#     cv2.imshow('img', img)
#     cv2.waitKey(0)


# cv2.destroyAllWindows()
