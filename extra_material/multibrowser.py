from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.get("https://www.youtube.com/")
print(driver.title)  # this will give the title of the page
print(driver.current_url)
driver.close()
