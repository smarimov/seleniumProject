from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get("https://www.facebook.com/")

username = driver.find_element_by_name("email")
print(username.is_displayed())  # returns true/false

print(username.is_enabled())  # return true/false

password = driver.find_element_by_name("pass")

print(password.is_displayed())  # returns true/false

print(password.is_enabled())  # return true/false

# This codes inputs your username and password:

username.send_keys("shokir92@gmail.com")
password.send_keys("Topsecret1234#")

login = driver.find_element_by_name("login")
login.click()

home = driver.find_element_by_xpath(
    '//*[@id="mount_0_0_n9"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a')

print(home.is_selected())
