from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")

driver.get('https://www.yahoo.com/?guccounter=1')

#driver.save_screenshot('C:\\Users\\shoki\\OneDrive\\Desktop\\screenshots\\homepage.png')

driver.get_screenshot_as_file('C:\\Users\\shoki\\OneDrive\\Desktop\\screenshots\\homepage2.png')
driver.quit()