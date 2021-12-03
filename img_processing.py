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
    grayed = cv2.bilateralFilter(grayed, 11, 17, 17) # Might need to adjust this
    edgedImg = cv2.Canny(grayed, 100, 200)

    # Using the modified image to find the contours in the image, place all found contours in a list 
    edges, new = cv2.findContours(edgedImg.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    edges = sorted(edges, key=cv2.contourArea, reverse=True) #[:30], might need to adjust this

    plateContour = None
    plate = None

    # This loop goes through all the contours in the list and tries to find the one 
    # most similarly correlated to a license plate by using corners
    for c in edges:
        perim = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perim, True) # or 0.02, might need to adjust this
        
        # If the approximation gets 4 corners, then that should hopefully be the license plate
        if len(approx) == 4:
            plateContour = approx
            x, y, w, h = cv2.boundingRect(c)
            # plate = grayed[y:y+h, x:x+w]
            plate = img[y+40:y+h-30, x+20:x+w-20]
            break
    
    # Temporarily testing output
    threshold, outImg = cv2.threshold(plate, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("License Plate Detection", outImg)
    cv2.waitKey(0)
    return outImg

def plate_to_text(img):
    # Maybe use the Medium website for this instead, it's only two lines of code from there
    text = pytesseract.image_to_string(img, config='--psm 11')
    
    # Typical Illinois plates have a length of 7-8 characters, and usually have a mix of Capital Letters and Numbers
    lines = text.splitlines()
    for line in lines:
        if len(line) == 7 or len(line) == 8:
            return line
    
    '''
    text = pytesseract.image_to_string(img, lang ='eng', config ='--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return text
    '''

    '''
    text = pytesseract.image_to_string(img, config='--psm 6')
    image = cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0))
    image = cv2.putText(image, text.upper(), (x+50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    print("License Plate: ", text.upper())
    cv2.imshow("License Plate Detection", image)
    cv2.waitKey(0)
    '''

# Temporarily running function
img = plate_recognition("test_pics/il10.jpg")
print(plate_to_text(img))