from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get("https://www.facebook.com/")
print(driver.title)
sleep(3)

driver.get("https://www.instagram.com/")
print(driver.title)
sleep(3)

driver.back()
print(driver.title)
sleep(3)

driver.forward()
print(driver.title)
sleep(3)
