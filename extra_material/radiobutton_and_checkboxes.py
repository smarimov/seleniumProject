from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfBVMyfz2anjnyuyLljeok7coZJpseibdPo6BAT0JyLwQmxMg/viewform')

# working with radio buttons
# first we check if the radio button is NOT selected by default using this:  is_selected
status = driver.find_element_by_xpath('//*[@id="i13"]/div[3]/div/div').is_selected()
print(status)

# click on the radio button:
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll the page
driver.find_element_by_xpath('//*[@id="i13"]/div[3]/div').click()

status = driver.find_element_by_xpath('//*[@id="i13"]/div[3]/div').is_selected()
print(status)

# working with checkboxes