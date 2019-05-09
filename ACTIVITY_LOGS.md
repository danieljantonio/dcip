### 9/5
- removed useless functions from east_resize
- resize32 function now requires an n parameter for the divisible value of the image
- screenshot.grab() now returns the proper image dimensions for EAST as previously it returned an image of a `[1080, 1920, 4]` dimension 
east now works properly
east_resize now only contains resize32 function, and requires an n parameter for what is to be divided
screenshot.grab() now returns the proper dimensions for the image that could be processed by east

### 8/5
- ImageGrab is takes a minimum of 0.3 seconds for each screenshot, this is now converted with python mss function to screenshot which takes at most 0.11 seconds for each screenshot
- improved the bg_changes by applying additional dilation and erosion to the mask, the erosion has also been increased in order to reduce the overall roi and remove any false positives

### 6/5
- may have found a better way to use EAST text detector https://www.learnopencv.com/deep-learning-based-text-detection-using-opencv-c-python/
- https://cloud.google.com/vision/docs/ocr check out google's text detector

### 3/5
- calculated the average time of bg_changes, which is under 0.11 seconds and averaged around 0.09 seconds
- researching on a way to combine small contours into one big contour

### 2/5
- researched on python multithreading and multiprocessing

### 25/4
- trying a good thresholding in order to reverse white text with black background
- used np.mean in order to have a different thresholding when the background is black and the text is white
- when using cv2.THRESH_BINARY_INV, the text is outlined by a white border
- the reason for the border is because the text is being smoothed and its not all white, hence the reason for the outline border
- found this link https://medium.freecodecamp.org/getting-started-with-tesseract-part-ii-f7f9a0899b3f 

### 24/4
- attempted to use cv2.cvtColor to conver the image to grayscale, then used adaptive thresholding in order to get a binary image
- to be done (send binary image to be used for the EAST detection, need to calibrate the functions)


### 23/4
- discovered a list of bad words that are banned by google, youtube, and facebook from https://www.freewebheaders.com that contains more than 1000 profanity words
- discovered a shorter list of words from the same website
- discovered a different list of bad words from cs.cmu.edu that contains over 1000 profanity words
- included tesseract_ocr in the main function, currently it still takes a bit too long

### 17/4 
- added non_max_suppression to bg_changes
- work from home -> tested on 2 monitors
- added east_resize to calculate the size of the image, divide it by 3, and make sure that its divisible by 32
- changed function names
- added ocr functions to tesseract_ocr
- preparing the functions to be combined (bg_changes ROIs and detect_text)


### 12/4
- tried using pyscreenshot to record the screen
- trying to figure out how to screenshot every 2 seconds
- started combining east and bg_changes
- changed bg_changes to be able to receive no prev image
- tried using the bg_changes in main with the screen record, dilate shows white, grey, and black for some reason, still trying to figure out the missing link


### 11/4
- finished adding bg_changes detect_changes function
- resize image to smaller size
- uses createBackgroundSubtractorMOG2 to get the difference
- a kernel of size 9x9 and dilate the small missing pieces
- find contours after dilating the frame
- extracted the ROIs and return the roi from the original image
- created tesseract_ocr.py
- added import for east and bg_changes on main.py


### 10/4
- started working on bg_changes
- experimentation on contours
- tried to find a way to merge multiple contours together and send an image that contains all the contours
