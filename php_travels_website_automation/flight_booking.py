from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://phptravels.net/home')


driver.find_element_by_xpath('//label[@for="flightSearchRadio-1"]').click()
sleep(2)

origin = driver.find_element_by_xpath('//div[@id="s2id_location_from"]')
origin.click()

