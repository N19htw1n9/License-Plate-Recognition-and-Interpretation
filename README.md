
# License Plate Recognition + Interpretation

**By Sarim Qureshi (squres25), Daniel Levert (dlever2), Zak Jamal (zmjamal2), Mohammed Akif (makif3), Tosan Egbesemirone (oegbes2)**

## Abstract

## 1. Introduction
This project is designed to be a license plate recognition and interpretation program. The program takes an input image and detects a license plate from the image (using cropping, filtering, and edge detection techniques with the OpenCV library). The plate is then cropped and sent to a function that is responsible for recognizing the text written on the plate (using text recognition techniques with the Tesseract OCR library). Then the text is passed to an automation script (with the Selenium WebDriver library), which navigates to a car recognition database [FAXVIN](https://www.faxvin.com/license-plate-lookup), whereupon the script will search the license plate and retrieve the car's information. The program will then output the license plate, VIN, Year, Make, and Model of the queried car onto the terminal.

### 1.1. Process

### 1.2. Language + Requirements
This program was designed using Python 3.6 and it's libraries:
 - OpenCV
 - Tesseract OCR
 - Selenium WebDriver
 - unittest
 - sys
 - os
 - time

The program also has a specific browser specification:

 - Google Chrome, Version 97 or earlier

## 2. Installation and Configuration

### 2.1. For Mac
 **1. Download tesseract *(with Homebrew)***
```
> brew install tesseract
```
	
 **2. Download pytesseract**
```
> pip install pytesseract
```
OR
```
> pip3 install pytesseract
```
	
 **3. Configure Tesseract path**
Comment out line 15 of img_processing.py
```
15   # pytesseract.pytesseract.tesseract_cmd = r"[PATH]"
```
Since Mac does not require a .exe installation for tesseract, we do not need to give a path variable
	
 **4. Download OpenCV**
```
> pip install opencv-python
```
OR
```
> pip3 install opencv-python
```

 **5. Download Chrome WebDriver**
Download the driver version corresponding to the version of Chrome you have as well as your operating system from [https://chromedriver.chromium.org/downloads](https://www.faxvin.com/license-plate-lookup).

 **6. Configure WebDriver path**
Extract the `chromedriver` file into `/usr/local/bin/`. Then comment out line 23 of `automation_script.py` and uncomment line 25
```
23   # PATH = executable_path='chromedriver.exe'
```
```
25   PATH = executable_path='/usr/local/bin/chromedriver'
```

### 2.2. For Windows

 **1. Download tesseract**
```
> pip install tesseract
```
OR
```
> pip3 install tesseract
```

 **2. Download pytesseract**
```
> pip install pytesseract
```
OR
```
> pip3 install pytesseract
```
	
 **3. Configure Tesseract path**
Navigate to this [installer page](https://github.com/UB-Mannheim/tesseract/wiki), download the setup wizard pertaining through your system, and run the executable. Copy the path shown during this step of the setup:

![Path](https://i.ibb.co/2WjmDWN/install.png)

This is where your `tesseract.exe` file will be located. Upon installation, navigate to the copied path, ensure that `tesseract.exe` is there, copy it's path, and place it onto the string placeholder of line 17 in `img_processing.py`

```
17   pytesseract.pytesseract.tesseract_cmd = r"[PATH]"
```
	
 **4. Download OpenCV**
```
> pip install opencv-python
```
OR
```
> pip3 install opencv-python
```

 **5. Download Chrome WebDriver**
Download the driver version corresponding to the version of Chrome you have as well as your operating system from [https://chromedriver.chromium.org/downloads](https://www.faxvin.com/license-plate-lookup).

 **6. Configure WebDriver path**
Extract the `chromedriver.exe` file into your project directory. Then uncomment line 23 of `automation_script.py` and comment out line 25
```
23   PATH = executable_path='chromedriver.exe'
```
*Note: You may need to give the absolute path for* `chromedriver.exe` *in which case, edit line 24*

```
25   # PATH = executable_path='/usr/local/bin/chromedriver'
```

## 3. Constraints

-   Input file types are limited to .jpeg and .jpg extensions
-   License plate must be visible and of a rectangular or almost rectangular shape in the image
-   License plate must be from Illinois
-   The text of the license plate has to be of length greater than or equal to 7
-   Input image must not be too reflective or too bright

## 4. Fail Cases
`fail1.jpg`  and `fail4.jpg`
When these images are being processed, the grill is captured instead of the plate. This is likely because the program interprets the grill as an almost rectangular shape.

`fail2.jpg` 
When this image is being processed, some random rectangular-like shaped is captured in the corner. This is likely because of the high brightness the window of the car generates, which confuses the program.

`fail3.jpg` 
When this image is being processed, the program captures the ledge located above the license plate. This is likely because the shading difference between the right and left side of the original image confuses the program into thinking the location of the plate actually consists of two different entities.

`fail4.jpg` 
When this image is being processed, the program captures the grill of a car that is reflected off the car intended to be captured. Due to the nature of some car paint being reflective, the program is unable to differentiate between multiple solid entities.

`fail5.jpg` 
When this image is being processed, the program captures a portion of the license plate that it deems to be rectangular-like. This is likely because of the angle at which the picture shows the license plate to be.

`fail6.jpg` 
When this image is being processed, the program captures practically nothing. This is likely due to the overall high brightness of the entire image itself.

### 4.1. Other Fail Cases


### 4.2. Discussion
In terms of processing an image and extracting its plate, this program is not without flaw. The conditions of the image (brightness, reflectivity, angle, background noise) are all major factors that determine the optimal output. The best conditions have been noted to be when a picture is taken during the middle of the day (due to the neutral brightness of the sun), from 5+ feet away, zoomed in to reduce the maximum amount of background noise, and at a perfectly straight angle.

## 5. Run


### 5.1. Run Test Cases


## 6. References
