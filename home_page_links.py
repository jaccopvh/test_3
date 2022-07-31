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


class TestTest:
    def __init__(self, test_case, test_result):
        self.test_case = test_case
        self.test_result = test_result

    def setup_method(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\jacco\Google Drive\QC\chromedriver_win32\chromedriver.exe')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        self.driver.maximize_window()
        self.driver.get("https://www.porvainn.eu")
        try:
            assert self.driver.find_element(By.XPATH, "(//a[contains(text(),\'prices and bookings\')])[2]").text == "prices and bookings"
            self.test_result = True
        except:
            self.test_result = False
        self.driver.close()


Jacco = TestTest('Check menu items', False)
Jacco.setup_method()
Jacco.test_test()
Jacco.teardown_method()

print(Jacco.test_case + ': ' + str(Jacco.test_result))
