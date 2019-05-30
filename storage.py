import cv2
import os
from imutils import paths
from time import time

def cache(image, filename):
    cv2.imwrite('.cache/{}.jpg'.format(filename), image)

def clear_old_cache(age):
    cachePath = list(paths.list_images('.cache'))
    for (i, img) in enumerate(cachePath):
        filename = img.split(os.path.sep)[-1]
        filename = filename.replace('.jpg','')
        if (int(time()) - int(filename)) > age:
            os.remove(img)

# clear_old_cache(15)