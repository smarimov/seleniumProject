from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")

driver.get('https://www.target.com/guest/gift-card-balance')

giftcard_number = driver.find_element_by_id('giftCardNumber')
giftcard_number.send_keys('041222193795144')

giftcard_pin = driver.find_element_by_id('accessNumber')
giftcard_pin.send_keys('60635642')

check_balance_button = driver.find_element_by_id('queryGiftCard')
check_balance_button.click()