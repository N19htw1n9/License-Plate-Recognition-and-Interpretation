# Assigned to Zak, Tosan, and Sarim

'''
Links:
https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/
https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c - main reference
https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/
https://youtu.be/0-4p_QgrdbE
'''

import cv2
import pytesseract

# Place the location of the downlaoded pytesseract executable here
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sarim\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def plate_recognition(path):

    # Applying filters and canny edge detection to the image to make it easily readable by using OpenCV
    img = cv2.imread(path)
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
            # plate = img[y:y+h, x:x+w] # Semipasses with pass2.jpg, semipass5.jpg. Passes with semipass1.jpg. Fails with semipass2.jpeg, semipass4.jpg
            plate = img[y+30:y+h-20, x:x+w] # Passes with pass1.jpg, pass2.jpg. Semipasses with semipass1.jpg, semipass2.jpeg, semipass3.jpeg, semipass4.jpg, semipass5.jpg
            # plate = img[y+40:y+h-30, x+20:x+w-20] # Passes with pass2.jpg, semipass1.jpg, semipass2.jpeg. Almost fails with pass1.jpg. Fails with semipass2.jpeg, semipass4.jpg. Semipasses with semipass5.jpg
            break
    
    threshold, outImg = cv2.threshold(plate, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("License Plate Detection", outImg)
    cv2.waitKey(0)
    return outImg

def plate_to_text(img):
    text = pytesseract.image_to_string(img, config='--psm 11')
    
    # Typical Illinois plates have a length of 7-8 characters, and usually have a mix of Capital Letters and Numbers
    lines = text.splitlines()
    for line in lines:
        if len(line) >= 7:
            return line