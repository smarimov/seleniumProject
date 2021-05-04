from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?allclasses-index.html')

# find element of the frame you want to swtich to
driver.switch_to_frame('packageListFrame')

# find the element of particular link in the chosen frame:
driver.find_element_by_link_text('org.openqa.selenium').click()
time.sleep(3)

# Get back to main page to switch to second frame:
driver.switch_to_default_content()

# Switch to second frame:
driver.switch_to.frame('packageFrame')

driver.find_element_by_link_text('WebDriver').click()
time.sleep(3)

#swtich to third frame
driver.switch_to_default_content()
driver.switch_to.frame('classFrame')
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]/a').click()
