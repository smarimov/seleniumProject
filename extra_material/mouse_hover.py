from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://mail.ru/')

driver.find_element_by_name('login').send_keys('shokirbeck17@mail.ru')
driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]').click()

driver.find_element_by_name('password').send_keys('youth')
driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[2]').click()

vse_proekti = driver.find_element_by_link_text('Все проекты')
moy_mir = driver.find_element_by_link_text('Мой Мир')

actions = ActionChains(driver)
actions.move_to_element(vse_proekti).move_to_element(moy_mir).click().perform()
