from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import *

driver = webdriver.Chrome()
# or webdriver.Chrome('/path/to/chromedriver')
sleep(5)

driver.get("https://google.com")

search_text_box = driver.find_element(By.NAME, "q")
search_text_box.clear() #delete everything in the search box
search_text_box.send_keys("python selenium integration") #typing in the search box
search_text_box.send_keys(Keys.RETURN) #hitting the enter key
