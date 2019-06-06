import cv2

def changes(img):
    change = 0
    current = 0
    for i in img:
        for j in i:
            if j != current:
                change += 1
                current = j
    return change

def midsection(img, iteration = 0):
    h, w = img.shape[:2]
    mid_point = int(h/2)
    point1 = mid_point + iteration
    point2 = mid_point + iteration + 1
    line_img = img[point1:point2, :]
    edges = cv2.Canny(line_img,100,200)
    return edges, point1

def split_image(img):
    textLine = True
    iteration = 0
    h, w = img.shape[:2]
    while textLine and iteration < 50:
        edge, point = midsection(img, iteration)
        change = changes(edge)
        if (change/w) < 0.3:
            textLine = False
        iteration += 3
    if textLine == False:
        return (img[:point, :], img[point:, :])
