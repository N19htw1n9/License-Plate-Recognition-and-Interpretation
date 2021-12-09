# Assigned to Zak, Tosan, and Sarim

'''
Links:
https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/
https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c - main reference
https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/
'''

import cv2
import pytesseract
from sys import platform
import os

# Place the location of the downlaoded pytesseract executable here
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sarim\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def plate_recognition(path):
    # Applying filters and canny edge detection to the image to make it easily readable by using OpenCV
    
    img = None
    try:
        img = cv2.imread(path)
    except:
        if platform == "win32" or platform == "win64":
            os.system('cls')
            print("Error: File not found")
            quit()
        else:
            os.system('clear')
            print("Error: File not found")
            quit()
    
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayed = cv2.bilateralFilter(grayed, 11, 17, 17)
    edgedImg = cv2.Canny(grayed, 100, 200)

    # Using the modified image to find the contours in the image, place all found contours in a list 
    edges, new = cv2.findContours(edgedImg.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    edges = sorted(edges, key=cv2.contourArea, reverse=True)

    plateContour = None
    plate = None

    # This loop goes through all the contours in the list and tries to find the one 
    # most similarly correlated to a license plate by using corners
    for c in edges:
        perim = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perim, True)
        
        # If the approximation gets 4 corners, then that should hopefully be the license plate
        if len(approx) == 4:
            plateContour = approx
            x, y, w, h = cv2.boundingRect(c)
            try:
                # plate = img[y:y+h, x:x+w]
                plate = img[y+30:y+h-20, x:x+w]
                # plate = img[y+40:y+h-30, x+20:x+w-20]
            except:
                if platform == "win32" or platform == "win64":
                    os.system('cls')
                    print("Error: Window size constraint does not allow for this image to be processed")
                    quit()
                else:
                    os.system('clear')
                    print("Error: Window size constraint does not allow for this image to be processed")
                    quit()
            break
    
    threshold, outImg = cv2.threshold(plate, 80, 255, cv2.THRESH_BINARY)
    # cv2.imshow("License Plate", outImg)
    cv2.waitKey(0)
    return outImg

def plate_to_text(img):
    text = pytesseract.image_to_string(img, config='--psm 11')
    
    # Typical Illinois plates have a length of 7-8 characters, and usually have a mix of Capital Letters and Numbers
    lines = text.splitlines()
    for line in lines:
        if len(line) >= 7:
            return line
    
    print("Error: Unable to extract license plate")
    quit()