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
