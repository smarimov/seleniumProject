from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://www.facebook.com/')
#wait some time here

driver.implicitly_wait(10) #seconds

assert "Facebook - Log In or Sign Up" in driver.title

username = driver.find_element_by_name("email")
username.send_keys("shokir92@gmail.com")

password = driver.find_element_by_name("pass")
password.send_keys("Topsecret1234#")

login = driver.find_element_by_name("login")
login.click()
