from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")

driver.get('https://www.amazon.com/')

#Capture all the cookies:

cookies = driver.get_cookies()
print(len(cookies))

#Adding new cookie to the browser:
cookie = {'name': 'my_cookie', 'value':'12345678'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))


#Deleting a cookie:
driver.delete_cookie('my_cookie')
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

driver.quit()