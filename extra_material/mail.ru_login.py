from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.implicitly_wait(20)
driver.get('https://mail.ru/')

driver.find_element_by_name('login').send_keys('shokirbeck17@mail.ru')
driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]').click()

driver.find_element_by_name('password').send_keys('youth')
driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[2]').click()