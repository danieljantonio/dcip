# import packages
from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
from imutils import resize
import numpy as np
import argparse
import time
import cv2

from screenshot import grab

def detect_text(image, height=544, width=960, min_confidence=0.5, padding=0.05):
    start = time.time()
    
    # save a copy of the image
    original_image = image.copy()

    # get size of image
    (origH, origW) = image.shape[:2]
    (newH, newW) = (height, width)

    # get ratio of original image to the new image
    ratio_h = origH / float(newH)
    ratio_w = origW / float(newW)

    # resize image to new image size
    image = cv2.resize(image, (newW, newH))
    (H, W) = image.shape[:2]

    # define the two output layers for the east detector model
    # one to output probabilities
    # one to derive bounding box of the text
    layerNames = [
        "feature_fusion/Conv_7/Sigmoid",
        "feature_fusion/concat_3"
    ]
    
    print("[info] loading EAST text detector...")
    net = cv2.dnn.readNet("east/frozen_east_text_detection.pb")

    blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False) # pre-trained RGB mean values
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)

    # get rows and cols from the scores
    # initialize the variable to store the rectangles and confidences
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    conf = []


    for y in range(0, numRows):
        # extract the scores(probabilities of a text)
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        for x in range(0, numCols):
            # if the score is less than our desired confidence, then just ignore it
            if scoresData[x] < min_confidence:
                continue

            # compute the offset factor, as the result image is going to be 4x smaller 
            (offsetX, offsetY) = (x * 4.0, y * 4.0)

            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            # using geometry volume to get the width and height of the bounding boxes
            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            # calculate the starting and ending coordinates for the text prediction boxes
            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)

            # add the coordinates and probability score to the list
            rects.append((startX, startY, endX, endY))
            conf.append(scoresData[x])

    # supress weak and overlapping boxes from the coordinates
    boxes = non_max_suppression(np.array(rects), probs=conf)

    roi = []
    # loop through bounding boxes
    for (startX, startY, endX, endY) in boxes:

        # scale the bounding boxes based on the ratios
        startX = int(startX * ratio_w)
        startY = int(startY * ratio_h)
        endX = int(endX * ratio_w)
        endY = int(endY * ratio_h)

        # add padding to the roi coordinates for better OCR
        dX = int((endX - startX) * padding)
        dY = int((endY - startY) * padding)

        # apply padding to each side of the bounding box, respectively
        startX = max(0, startX - dX)
        startY = max(0, startY - dY)
        endX = min(origW, endX + (dX * 2))
        endY = min(origH, endY + (dY * 2))

        # cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        # ret, roiBinary = cv2.threshold(roi, 100, 255, cv2.THRESH_BINARY)
        roi.append(original_image[startY:endY, startX:endX])
        # todo
        # try and resize the images in the roi for better ocr, rever to https://medium.freecodecamp.org/getting-started-with-tesseract-part-ii-f7f9a0899b3f for possible optimizations
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
        
    end = time.time()

    print("[INFO] text detection took {:.6f} seconds".format(end-start))
    return (roi, image)

# img = grab()
# print(img.shape)

# rois, img = detect_text(img)
# for img in rois:
#     cv2.imshow('img', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
