from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")


def bestbuy(gc_number, gc_pin_code):
    url_bestbuy = 'https://www.bestbuy.com/gift-card-balance?ref=212&loc=1&ds_rl=1268664&gclid=Cj0KCQjwyN-DBhCDARIsAFOELTkaMgSY0nrZ8q_GK4O1X013LYUR7E2aiAturlheAUjOCyucUdst4aYaAifnEALw_wcB&gclsrc=aw.ds'

    driver.get(url_bestbuy)

    driver.find_element_by_id("gift-card-number").send_keys(gc_number)
    driver.find_element_by_id("pin-number").send_keys(gc_pin_code)
    button = driver.find_element_by_xpath("//button[contains(text(),'Check Balance')]")
    button.click()


def victoria_secret(gc_number, gc_pin_code):
    driver.get('https://www.victoriassecret.com/us/vs/gift-cards')
    gcnumber_element = driver.find_element_by_id('gcNumber')
    gcnumber_element.send_keys(gc_number)
    gcpin_element = driver.find_element_by_id('gcPin')
    gcpin_element.send_keys(gc_pin_code)
    check_balance_button = driver.find_element_by_xpath("//button[@type='submit']")
    check_balance_button.click()


def dicks(gc_number, gc_pin_code):
    driver.get('https://www.dickssportinggoods.com/s/gift-cards')
    gc_number_element = driver.find_element_by_name('gcNumber')
    gc_number_element.send_keys(gc_number)
    gc_pin_element = driver.find_element_by_id('giftcard-pinnum')
    gc_pin_element.send_keys(gc_pin_code)
    check_balance_button = driver.find_element_by_id('giftCardForm_balanceCheck')
    check_balance_button.click()


def home_depot(gc_number, gc_pin_code):
    driver.get('https://secure2.homedepot.com/mycheckout/giftcard#/giftcard')
    gc_number_element = driver.find_element_by_name('giftCardNumber')
    gc_number_element.send_keys(gc_number)
    gc_pin_element = driver.find_element_by_name('PINNumber')
    gc_pin_element.send_keys(gc_pin_code)

bestbuy('6163630849448255', '9052')
