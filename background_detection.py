from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
import cv2
import numpy as np
from imutils import resize
from time import time, sleep

def background_changes(new_frame, previous_frame, new_h=544, new_w=960):
    fnStart = time()
    original_frame = new_frame.copy()
    (frame_h, frame_w) = original_frame.shape[:2]
    ratio_h = frame_h / new_h
    ratio_w = frame_w / new_w

    frame1 = cv2.resize(previous_frame, (new_w, new_h))
    frame2 = cv2.resize(new_frame, (new_w, new_h))

    fgbg = cv2.createBackgroundSubtractorMOG2()

    frames = [frame1, frame2]

    rects = []
    roi = []

    fgmask = fgbg.apply(frame1)
    fgmask = fgbg.apply(frame2)
    # cv2.imshow('fgmask', fgmask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    kernel = np.ones((3,5), np.uint8)
    dilate = cv2.dilate(fgmask, kernel, iterations=2)
    # cv2.imshow('dilate1', dilate)
    closing = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('closing', closing)
    erode = cv2.erode(closing, kernel, iterations=7)
    # cv2.imshow('erode', erode)
    kernel = np.array([[0,0,0,0,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,0,0,0,0]], np.uint8)
    dilate = cv2.dilate(erode, kernel, iterations=5)
    # cv2.imshow('dilate2', dilate)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # rectsimg = original_frame.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        start_x = int(x * ratio_w)
        start_y = int(y * ratio_h)
        end_x = int((x+w) * ratio_w)
        end_y = int((y+h) * ratio_h)

        rects.append((start_x, start_y, end_x, end_y))
        # cv2.rectangle(rectsimg, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
    boxes = non_max_suppression(np.array(rects))
    
    # boxesimg = original_frame.copy()
    for (start_x, start_y, end_x, end_y) in boxes:
        x = end_x-start_x
        y = end_y-start_y
        if ( x > 150 and y > 150):
            img_frame = original_frame[start_y:end_y, start_x:end_x] 
            img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
            img_mean = int(img_frame.mean())
            if img_mean > 127:
                ret, thresh = cv2.threshold(img_frame, img_mean, 255, cv2.THRESH_BINARY)
            else:
                ret, thresh = cv2.threshold(img_frame, img_mean, 255, cv2.THRESH_BINARY_INV)
            # cv2.imshow('im', thresh)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            roi.append(thresh)

    fnEnd = time()
    # print('[info] background_detection took  = {:.4f} seconds'.format(fnEnd-fnStart))
    return roi
