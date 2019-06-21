import cv2
import os
from imutils import paths
from time import time

def cache(image, filename):
    # save image to .cache folder
    cv2.imwrite('.cache/{}.jpg'.format(filename), image)

def clear_old_cache(age):
    # create a list of the images in the .cache folder
    cachePath = list(paths.list_images('.cache'))
    # for each image in the folder
    for (i, img) in enumerate(cachePath):
        # the file path is removed
        filename = img.split(os.path.sep)[-1]

        # the file type is removed
        filename = filename.replace('.jpg','')

        # images with timestamps (filename) who's age is bigger is removed 
        if (int(time()) - int(filename)) > age:
            os.remove(img)
