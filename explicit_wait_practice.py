import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def test1_text_to_present():
    print("Case1:")

    print("Open browser")
    driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

    print("Clicking on 'Change Text to Selenium WebDriver'")
    element1 = driver.find_element_by_id('populate-text').click()

    print("Waiting for the text to appear")
    wait = WebDriverWait(driver, 30)
    msg_xpath = "//h2[@id='h2']"
    ext_text = "Selenium Webdriver"
    msg = wait.until(EC.text_to_be_present_in_element((By.XPATH, msg_xpath), ext_text))

    print("Printing the message:")
    print(f'Message printed: "{msg}"')
    print('Case1 complete')


def test2_visibility_of_element():
    print("Case2:")

    print("Open Browser")
    driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

    print("Clicking on 'Display' button")
    element1 = driver.find_element_by_id('display-other-button').click()
    print("Waiting for 'enabled' button appear ")
    enabled_xpath = "//button[@id='hidden']"
    wait = WebDriverWait(driver, 30)
    enabled_button = wait.until(EC.visibility_of_element_located((By.XPATH, enabled_xpath)))

    print("Clicking on 'enabled' button appear")
    enabled_button.click()

    print("Waiting for 'enabled' button disappear")
    button_disappear = wait.until_not(EC.visibility_of_element_located((By.XPATH, enabled_xpath)))

    print("Case2 completed")


def test3_element_to_be_clickable():
    print("Case3:")
    print("Opening browser")
    driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    print("Clicking on the button")
    element3 = driver.find_element_by_id('enable-button').click()
    print("Waiting for the second button to appear")
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#disable')))
    print("Case 3 completed")
