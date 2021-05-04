import option as option
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path="C:\\Program Files\\Python39\\chromedriver")

driver.get('https://www.facebook.com/messages/t/100005441689353')

driver.find_element_by_id('email').send_keys("shokir92@gmail.com")

driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Topsecret1234#')

driver.find_element_by_xpath("//label[@id='loginbutton']").click()

time.sleep(10)

# while True:
    message = driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div["
                                       "2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                       "2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                                       "1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")

    message.send_keys('hi')

    driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/span[2]/div[1]").click()