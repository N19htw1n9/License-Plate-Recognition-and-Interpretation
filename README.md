
# License Plate Recognition + Interpretation

**By Sarim Qureshi (squres25), Daniel Levert (dlever2), Zak Jamal (zmjamal2), Mohammed Akif (makif3), Tosan Egbesemirone (oegbes2)**

This project is designed to be a license plate recognition and interpretation program. The program takes an input image and detects a license plate from the image (using cropping, filtering, and edge detection techniques with the OpenCV library). The plate is then cropped and sent to a function that is responsible for recognizing the text written on the plate (using text recognition techniques with the Tesseract OCR library). Then the text is passed to an automation script (with the Selenium WebDriver library), which navigates to a car recognition database [FAXVIN](https://www.faxvin.com/license-plate-lookup), whereupon the script will search the license plate and retrieve the car's information. The program will then output the license plate, VIN, Year, Make, and Model of the queried car onto the terminal.

## Requirements
This program was designed using Python 3 and it's libraries:
 - OpenCV
 - Tesseract OCR
 - Selenium WebDriver
 - unittest
 - sys
 - os
 - time

The program also has a specific browser specification:

 - Google Chrome, Version 97 or earlier

## Installation and Configuration (for Mac)

 **1. Download tesseract**
```
brew install tesseract
```
	
 **2. Download pytesseract**
```
pip install pytesseract
```
OR
```
pip3 install pytesseract
```
	
 **3. Configure Tesseract path**
Comment out line 15 of img_processing.py
```
# pytesseract.pytesseract.tesseract_cmd = r"[PATH]"
```
Since Mac does not require a .exe installation for tesseract, we do not need to give a path variable
	
 **4. Download OpenCV**
```
pip install opencv-python
```
OR
```
pip3 install opencv-python
```

 **5. Download Chrome WebDriver**
Download the driver version corresponding to the version of Chrome you have as well as your operating system from [https://chromedriver.chromium.org/downloads](https://www.faxvin.com/license-plate-lookup).

 **6. Configure WebDriver path**
Extract the `chromedriver` file into `/usr/local/bin/`. Then comment out line 22 of `automation_script.py`
```
# PATH = executable_path='chromedriver.exe'
```
and uncomment line 23
```
PATH = executable_path='/usr/local/bin/chromedriver'
```

## Installation and Configuration (for Windows)

 **1. Download tesseract**
```
pip install tesseract
```
OR
```
pip3 install tesseract
```

 **2. Download pytesseract**
```
pip install pytesseract
```
OR
```
pip3 install pytesseract
```
	
 **3. Configure Tesseract path**
Navigate to this [installer page](https://github.com/UB-Mannheim/tesseract/wiki), download the setup wizard pertaining through your system, and run the executable. Copy the path shown during this step of the setup:

![Path](https://i.ibb.co/2WjmDWN/install.png)

This is where your `tesseract.exe` file will be located. Upon installation, navigate to the copied path, ensure that `tesseract.exe` is there, copy it's path, and place it onto the string placeholder of line 15 in `img_processing.py`

```
pytesseract.pytesseract.tesseract_cmd = r"[PATH]"
```
	
 **4. Download OpenCV**
```
pip install opencv-python
```
OR
```
pip3 install opencv-python
```

 **5. Download Chrome WebDriver**
Download the driver version corresponding to the version of Chrome you have as well as your operating system from [https://chromedriver.chromium.org/downloads](https://www.faxvin.com/license-plate-lookup).

 **6. Configure WebDriver path**
Extract the `chromedriver.exe` file into your project directory. Then uncomment line 22 of `automation_script.py`
```
# PATH = executable_path='chromedriver.exe'
```
*Note: You may need to give the absolute path for `chromedriver.exe`*

and comment out line 23
```
PATH = executable_path='/usr/local/bin/chromedriver'
```

## Constraints

-   Input file types are limited to .jpeg and .jpg extensions
-   License plate must be visible and of a rectangular or almost rectangular shape in the image
-   License plate must be from Illinois
-   The text of the license plate has to be of length greater than or equal to 7
-   Input image must not be too reflective or too bright

## Fail Cases
`fail1.jpg` When this image is being processed, the grill is captured instead of the plate. This is likely because the program interprets the grill as an almost rectangular shape.
