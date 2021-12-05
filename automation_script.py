# Assigned to Dan and Sarim

'''
Link to automate on:

https://www.faxvin.com/license-plate-lookup
'''

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def return_info(licensePlate):
    # For some reason, the geckodriver for firefox is being buggy so let's stick with Chrome for now
    PATH = executable_path='C:\\Users\\sarim\\Desktop\\CS415_Project\\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    plate, VIN, make, model, year = None, None, None, None, None

    try:
        driver.get("https://www.faxvin.com/license-plate-lookup/")

        driver.set_window_size(550, 691)
        driver.find_element(By.CSS_SELECTOR, "label").click()
        driver.find_element(By.NAME, "plate").click()
        driver.find_element(By.NAME, "plate").send_keys(licensePlate)
        driver.find_element(By.NAME, "state").click()
        dropdown = driver.find_element(By.NAME, "state")
        dropdown.find_element(By.XPATH, "//option[. = 'Illinois (IL)']").click()
        driver.find_element(By.CSS_SELECTOR, "option:nth-child(15)").click()
        driver.find_element(By.CSS_SELECTOR, "button").click()

        time.sleep(10)
        plate = licensePlate
        VIN = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/b").text
        make = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/b").text
        model = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/b").text
        year = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/b").text
    
    finally:
        driver.quit()

    return plate, VIN, make, model, year