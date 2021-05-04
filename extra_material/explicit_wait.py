from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  u

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
print("Opening the website")
driver.implicitly_wait(20)
driver.get("https://www.expedia.com/")

print("Clicking on 'Flights' ")
flights = driver.find_element_by_link_text('Flights')
flights.click()

print("Putting text in 'Origin'")
origin = driver.find_element_by_link_text('Leaving from')
origin.click()

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable)
"""
location = driver.find_element_by_xpath(
    '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]/div/div/div/button')
location.send_keys("TAS")

sleep(2)

destination = driver.find_element_by_xpath(
    '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[2]/div/div/div/button')
destination.send_keys('NYC')

departing_date = driver.find_element_by_xpath('//*[@id="d1-btn"]')
departing_date.send_keys('05/25/2021')

returning_date = driver.find_element_by_xpath('//*[@id="d2-btn"]')
returning_date.clear()
returning_date.send_keys('08/20/2021')

search = driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button')
search.click()
"""
