### 17/4 
- added non_max_suppression to bg_changes
- work from home -> tested on 2 monitors
- added east_resize to calculate the size of the image, divide it by 3, and make sure that its divisible by 32

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
