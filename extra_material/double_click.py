from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

# First find element
element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
actions.double_click(element).perform()
