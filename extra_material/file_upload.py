from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_id('RESULT_FileUpload-10').send_keys(
    "C://Users/shoki/OneDrive/Desktop/Class/04 Python Selenium/cat.jfif")
