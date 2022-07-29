from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(executable_path=r'C:\Users\jacco\Google Drive\QC\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.porvainn.eu')
driver.find_element_by_link_text("prices and bookings").click()
