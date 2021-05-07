import time

import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


@pytest.mark.skipp
def test_drag_and_drop():
    driver.get('https://the-internet.herokuapp.com/drag_and_drop')
    source = driver.find_element_by_id('column-a')

    target = driver.find_element_by_id('column-b')

    actions = ActionChains(driver)

    actions.drag_and_drop(source, target).perform()


def test_dropdown():
    driver.get('https://the-internet.herokuapp.com/dropdown')
    element = driver.find_element_by_id('dropdown')
    drp = Select(element)
    drp.select_by_value('1')


def test_file_upload():
    driver.get('https://the-internet.herokuapp.com/upload')
    path = "C:\\Users\\shoki\\OneDrive\\Desktop\\New Text Document.txt"
    choose_file = driver.find_element_by_id('file-upload')
    choose_file.send_keys(path)
    upload = driver.find_element_by_id('file-submit')
    upload.click()


def test_infinite_scroll():
    driver.get('https://the-internet.herokuapp.com/infinite_scroll')
    driver.execute_script("window.scrollBy(0,15000)", "")


def test_javascript_alerts():
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    js_alert = driver.find_element_by_xpath('//button[@onclick="jsAlert()"]')
    js_alert.click()
    time.sleep(3)

    driver.switch_to.alert.accept()

    time.sleep(3)
    js_confirm = driver.find_element_by_xpath('//button[@onclick="jsConfirm()"]')
    js_confirm.click()
    time.sleep(3)

    driver.switch_to.alert.dismiss()

    time.sleep(3)
    js_prompt = driver.find_element_by_xpath('//button[@onclick="jsPrompt()"]')
    js_prompt.click()
    time.sleep(3)
    driver.switch_to.alert.send_keys('Thank you')
    driver.switch_to.alert.accept()


def geolocation():
    driver.get('https://the-internet.herokuapp.com/geolocation')
    driver.find_element_by_xpath('//button[@onclick="getLocation()"]').click()

    wait = WebDriverWait(driver, 20)
    ext_text = '40.3963904'
    wait.until(EC.text_to_be_present_in_element((By.ID, 'lat-value'), ext_text))
    ext_text1 = '-80.0423936'
    wait.until(EC.text_to_be_present_in_element((By.ID, 'long-value'), ext_text1))

    latitude = driver.find_element_by_id('lat-value')
    print(f'Latitude: {latitude.text}')
    longitude = driver.find_element_by_id('long-value')
    print(f'Longitude: {longitude.text}')


def horizontal_slider():
    driver.get('https://the-internet.herokuapp.com/horizontal_slider')
    slider = driver.find_element_by_xpath("//input[@type='range']")
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider, xoffset=50, yoffset=0).perform()


def context_menu():
    driver.get('https://the-internet.herokuapp.com/context_menu')
    element = driver.find_element_by_id('hot-spot')
    actions = ActionChains(driver)
    actions.context_click(element).perform()
    driver.switch_to_alert().accept()


def key_presses():
    driver.get('https://the-internet.herokuapp.com/key_presses?')
    element = driver.find_element_by_id('target')
    time.sleep(5)
    element.send_keys(Keys.ENTER)


def multiple_windows():
    driver.get('https://the-internet.herokuapp.com/windows')
    click_here = driver.find_element_by_link_text('Click Here')
    click_here.click()
    handles = driver.window_handles
    print(handles)
    time.sleep(5)
    driver.switch_to.window(handles[1])
    text = driver.find_element_by_xpath("//div[@class='example']")
    print(text.text)
