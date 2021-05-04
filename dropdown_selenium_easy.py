from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")
driver.implicitly_wait(20)

driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')


element = driver.find_element_by_id('select-demo')
drp_select_day = Select(element)
drp_select_day.select_by_visible_text('Sunday')

element_multi = driver.find_element_by_id('multi-select')
drp_states = Select(element_multi)
drp_states.select_by_index(2)
drp_states.select_by_index(4)
drp_states.select_by_value('Texas')