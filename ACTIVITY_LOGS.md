### 10/6
- meeting with dr chia
- redid the introduction, problem statement, etc. added a few more references
- redid the objective

### 6/6
- added a function to split an image into 2 without cutting the text
- combined the function with the rest of the system
- further tested the system

### 30/5
- added clear_old_cache(age) function to remove old functions that are older than 'age' compared to current time
- the old system uses an if statement to check if there are too many active threads, this is now changed to a while loop that sleeps when the max number of threads has been reached until the threads has finished processing and has free up space
- cleaning up the folder and file structure of the code
- email now sends an attachment of the time the screenshot is taken

### 29/5
- starting the implementation of smtp mailing system
- successfully sent an email listing the profanity inducing sentences to the email

### 26/5
- tested the system on real time, works nicely, does not take too much cpu processing power except for certain bursts of pytesseract. the python code itself only takes less than 20% of cpu processing power
- if there is still time, it might be a good idea to find a way to decide if an image area contains text or not
- changed screenshot.py grab() to screenshot all of the displays available. calculating the average of 100 screenshots, screenshotting increases the time by just over a double of the old time, the old time took 0.0487s on the first test and 0.0502 seconds on the second test, whereas screenshotting both of the images took 0.1056 seconds for the first time and 0.1012 seconds for the second time

### 19/5
- added profanity_check together with the other parts of the code, got into some errors but is already solved 
- in the attempt to fix profanity_check i changed the output of the function into 3 return values, the sentence, the category of the sentence (whether it has profanity (1) or not (0)), and the probability of it having profanity. note: i might add my own calculations on how the category works based on the probability

### 17/5
- found a profanity filter created by github user vzhou842 https://github.com/vzhou842/profanity-check
- officially removed east.py from the final code
- added the thresholding to bg_changes.py
- tested output from bg_changes on tesseract_ocr, result is good. accuracy above 90% and is under 3 seconds
- started combining everything together untill tesseract_ocr, showing an adequate accuracy 

### 14/5
- reading more about text detection/localization and found this link https://stackoverflow.com/questions/39078999/how-to-recognize-text-regions-using-histogram on recognizing text regions using histograms. the idea came after reading the paper by Devadeep Shyam on his proposed text detection technique

### 13/5
- added binary thresholding based on tesseract_ocr.py based on the mean of the pixels
- considering to remove east.py as it does not perform as expected

### 10/5
- found out that pytesseract works really well with a chunk of text, and is better with white background

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
