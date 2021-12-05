# Driver program meant to tie img_processing.py and automation_script.py together

from automation_script import return_info

plate, VIN, make, model, year = return_info("AE2 9185")
print(plate)
print(VIN)
print(make)
print(model)
print(year)
# return_info(plate_to_text(plate_recognition(path)))