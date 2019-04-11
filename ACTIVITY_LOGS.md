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
