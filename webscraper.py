from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver.exe")

driver.get('https://www.youtube.com/user/Shokiro17')

driver.find_element_by_id('video-title').click()