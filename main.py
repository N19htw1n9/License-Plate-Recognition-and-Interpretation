# Driver program meant to tie img_processing.py and automation_script.py together

from img_processing import plate_recognition
from img_processing import plate_to_text
from automation_script import return_info
from sys import platform
import os

path = input("Enter image path (with extension): ")
img = plate_recognition(path)
plateText = plate_to_text(img)
plate, VIN, make, model, year = return_info(plateText)


if platform == "win32" or platform == "win64":
    os.system('cls')
else:
    os.system('clear')

print("\n\n--- OUTPUT ---\n")
print("License Plate:", plate)
print("VIN:", VIN)
print("Year:", year)
print("Make:", make)
print("Model:", model)
quit()