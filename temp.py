from imutils.object_detection import non_max_suppression # functions for openCV, packaging multiple functions based on one use
import cv2
import numpy as np
from imutils import resize



img1 = cv2.imread('east/img/frame1.png')
img2 = cv2.imread('east/img/frame2.png')
original_image = img2.copy()
(new_w, new_h) = (960, 544)
(img2_h, img2_w) = img2.shape[:2]
ratio_h = img2_h / new_h
ratio_w = img2_w / new_w

img1 = cv2.resize(img1, (new_w, new_h))
img2 = cv2.resize(img2, (new_w, new_h))
fgbg = cv2.createBackgroundSubtractorMOG2()

# morphology -> dilate
# make it that the difference is gonna be one chunk
# contour it, then bounding box to the thing
# extract those areas

imgs = [img1, img2]

rects = []
roi = []
first = True
kernel = np.ones((9,9), np.uint8)

fgmask = fgbg.apply(img1)
fgmask = fgbg.apply(img2)

dilate = cv2.dilate(fgmask, kernel, iterations=2)


contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    
    start_x = int(x * ratio_w)
    start_y = int(y * ratio_h)
    end_x = int((x+w) * ratio_w)
    end_y = int((y+h) * ratio_h)

    roi.append(original_image[start_y:end_y, start_x:end_x])

for img in roi:
    cv2.imshow('img', img)
    cv2.waitKey(0)


cv2.destroyAllWindows()
