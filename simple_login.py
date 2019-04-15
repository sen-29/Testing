
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("/home/ujjval/Downloads/chromedriver_linux64/chromedriver")
driver.get('http://127.0.0.1:5000/')
driver.find_element_by_name("username").send_keys("1234567890")
driver.find_element_by_name("password").send_keys("2000")
driver.find_element_by_name("username").submit()    

