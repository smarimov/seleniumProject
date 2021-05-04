from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")

driver.get('https://www.seleniumeasy.com/test/table-pagination-demo.html')


print(len(driver.find_element_by_xpath('//tbody/tr')))
