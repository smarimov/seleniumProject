from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfBVMyfz2anjnyuyLljeok7coZJpseibdPo6BAT0JyLwQmxMg/viewform")

# How to find how many inputboxes present in web page:
input_boxes = driver.find_elements(By.CLASS_NAME, 'quantumWizTextinputPaperinputInput exportInput')
print(len(input_boxes))

# How to provide value into text box:
first_name = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
first_name.send_keys('leo')

last_name = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last_name.send_keys('hayitov')

phone_number = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone_number.send_keys('4029171596')
# driver.quit()
