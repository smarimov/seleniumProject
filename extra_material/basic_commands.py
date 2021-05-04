from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
button = driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button')
button.click()
sleep(5)
driver.quit()