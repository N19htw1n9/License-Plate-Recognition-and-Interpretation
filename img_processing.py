# Assigned to Zak, Tosan, and Sarim

'''
Links:
https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/

https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c - main reference

https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/

https://youtu.be/0-4p_QgrdbE

'''

import cv2
import imutils
import numpy as np


img = cv2.imread('car4.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 400))
grayedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayedImg = cv2.bilateralFilter(grayedImg, 13, 15, 15)
edges = cv2.Canny(grayedImg, 30, 200)

contours = (cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE))
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

mask = np.zeros(grayedImg.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('car', new_image)
cv2.waitKey(0)