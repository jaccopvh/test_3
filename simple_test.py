import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

globals()

def test_case1():

    driver = webdriver.Chrome(
        executable_path=r'C:\Users\jacco\Google Drive\QC\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.porvainn.eu")

    try:
       title1 = driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[0]").text
       title2 = driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[1]").text
       title3 = driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[2]").text
       title4 = driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[3]").text
       title5 = driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[4]").text

       print(str(title1))
       print(str(title2))
       print(str(title3))
       print(str(title4))
       print(str(title5))

       assert title1 == "Holiday home for 14-18 persons"
       assert title2 == "galery"
       assert title3 == "prices * and bookings"
       assert title4 == "activities"
       assert title5 == "contact"

       test_result = True

    except:
        test_result = False
    driver.close()
    driver.quit()



test_case1()
