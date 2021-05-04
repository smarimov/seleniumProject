from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://www.google.com/')
print(driver.title)

driver.get('https://www.google.co.in/')

driver.quit()