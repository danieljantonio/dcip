# dcip
Detection of Cyber-bullying Using Image Processing


```
Daniel Jedidiah Antonio
15068893
```
Supervised by
```
Dr. Chia Wai Chong
```
### installation
make sure you have python, pip, and tesseract-ocr installed locally
```
pip install opencv-python
pip install mss
pip install imutils
pip install pytesseract
pip install profanity_check
```

### run
```
# navigate to the folder containing ./dcip
python3 dcip/
mkdir .cache
```

### Research
- [ ] Dynamic threads in python
- [ ] How much load does each thread add, is it worthed to use threads in consideration of performance, time, and power consumption?
- [ ] How to speed up an area with huge chunks of text
- [ ] EAST text detection using binary image
- [ ] How long does it take to binary threshold a small image
- [ ] Detect areas where the text is chunked together (try to increase the padding, then use non_max_suppression with a lower overlapThresh)