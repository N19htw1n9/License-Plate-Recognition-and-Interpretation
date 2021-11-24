# Assigned to Zak, Tosan, and Sarim

'''
Links:
https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/
https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c - main reference
https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/
https://youtu.be/0-4p_QgrdbE
'''

import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\ProgramFiles(x86)\Tesseract-OCR\tesseract.exe'

def plate_recognition(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayed = cv2.bilateralFilter(grayed, 11, 17, 17) # Might need to adjust this

    edgedImg = cv2.Canny(grayed, 100, 200)
    edges, new = cv2.findContours(edgedImg.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    edges = sorted(edges, key=cv2.contourArea, reverse=True) #[:30], might need to adjust this

    plateContour = None
    plate = None

    for c in edges:
        perim = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perim, True) # or 0.02, might need to adjust this
        
        if len(approx) == 4:
            plateContour = approx
            x, y, w, h = cv2.boundingRect(c)
            plate = grayed[y:y+h, x:x+w]
            break
    
    # Temporarily testing output
    threshold, outImg = cv2.threshold(plate, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("License Plate Detection", outImg)
    cv2.waitKey(0)

def plate_to_text(img):
    # Maybe use the Medium website for this instead, it's only two lines of code from there
    
    '''
    text = pytesseract.image_to_string(blackAndWhiteImage, config='--psm 6')
    image = cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0) 3)
    image = cv2.putText(image, text.upper(), (x+50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    print("License Plate: ", text.upper())
    cv2.imshow("License Plate Detection", image)
    cv2.waitKey(0)
    '''

# Temporarily running function
plate_recognition("test_pics/il7.jpg")