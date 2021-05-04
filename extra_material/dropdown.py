from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://www.formsite.com/templates/human-resources/employment-application-form/')

driver.find_element_by_xpath('//*[@id="imageTemplateContainer"]/img').click()

driver.execute_script("argument[0].scrollIntoView();", 'RESULT_RadioButton-11')

#first install above 'Select' package

#second: find the element and use Select



element = driver.find_element_by_id('RESULT_RadioButton-11')

drp = Select(element)

#select by visible text:

drp.select_by_visible_text('Intern')

#select by index:

#drp.select_by_index(2)

#select by value:

#drp.select_by_value('Radio-1')

