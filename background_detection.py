from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
import cv2
import numpy as np
from resize import resize_n
from time import time, sleep

def background_changes(new_frame, previous_frame):
    
    fnStart = time()

    # creates a copy of the current frame
    original_frame = new_frame.copy()

    # extracts the frame shape 
    (frame_h, frame_w) = original_frame.shape[:2]

    # frame resize size
    new_h = int(frame_h/3)
    new_w = int(frame_w/3)

    # getting current size and old size ratio
    ratio_h = frame_h / new_h
    ratio_w = frame_w / new_w

    # resize new frame and previous frame
    frame1 = cv2.resize(previous_frame, (new_w, new_h))
    frame2 = cv2.resize(new_frame, (new_w, new_h))

    # initialize background subtractor 
    fgbg = cv2.createBackgroundSubtractorMOG2()

    frames = [frame1, frame2]

    rects = []
    roi = []

    # apply the frames to the background subtraction
    fgmask = fgbg.apply(frame1)
    fgmask = fgbg.apply(frame2)

    # getting the mean of the image pixels for thresholding
    img_mean = int(fgmask.mean())

    # thresholding the image based on the mean
    ret, thresh = cv2.threshold(fgmask, img_mean, 255, cv2.THRESH_BINARY)

    # using a '1' kernel of 3x5, perform dilation to close holes in the mask
    kernel = np.ones((3,5), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=3)

    # find contours from the mask
    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # process each contour point found
    for cnt in contours:
        # getting the points for the bounding rectangle
        x, y, w, h = cv2.boundingRect(cnt)

        # resizing the points to its original size using the ratio stored
        start_x = int(x * ratio_w)
        start_y = int(y * ratio_h)
        end_x = int((x+w) * ratio_w)
        end_y = int((y+h) * ratio_h)

        # appending the resized points
        rects.append((start_x, start_y, end_x, end_y))

    # applied non max suppression to remove overlapping boxes
    boxes = non_max_suppression(np.array(rects))
    
    # processing each bounding box point after non max suppression
    for (start_x, start_y, end_x, end_y) in boxes:
        # get the height and width of the box
        x = end_x-start_x
        y = end_y-start_y
        
        # only boxes above the size of 150x150 are processed further
        if ( x > 150 and y > 150):
            # region of interest is taken from the current frame copy
            img_frame = original_frame[start_y:end_y, start_x:end_x] 

            # converted the region of interest into grayscale
            img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)

            # calculating the mean of the grayscale image to get a value for thresholding
            img_mean = int(img_frame.mean())

            # the image is thresholded based on their mean in order to get a region with white background and black text
            if img_mean > 127:
                ret, thresh = cv2.threshold(img_frame, img_mean, 255, cv2.THRESH_BINARY)
            else:
                ret, thresh = cv2.threshold(img_frame, img_mean, 255, cv2.THRESH_BINARY_INV)
            
            # thresholded image are appended together to be returned
            roi.append(thresh)

    # fnEnd = time()
    # print('[info] background_detection took  = {:.4f} seconds'.format(fnEnd-fnStart))
    return roi
