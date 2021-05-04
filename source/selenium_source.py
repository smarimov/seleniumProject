from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from extra_material.utilities_time import *

driver = webdriver.Chrome()
driver.implicitly_wait(20)


def open_website(url):
    try:
        driver.get(url)
        print(driver.title)
        "Now clicking the 'No Thanks' button"
        pop_up = driver.find_element_by_link_text('No,thanks!').is_displayed()

    except NoSuchElementException:
        print("Pop Up did not appear this time")


def back_forward():
    # screenshots
    img1 = f'./../screenshots\\{get_str_seconds()}_pic.png'
    img2 = f'./../screenshots\\{get_str_seconds()}_pic.png'
    driver.back()
    driver.get_screenshot_as_file(img1)
    time.sleep(5)
    driver.forward()
    driver.get_screenshot_as_file(img2)
    time.sleep(5)


def get_total_input_fields(num1, num2):
    # inputs
    driver.find_element_by_id('sum1').send_keys(num1)

    driver.find_element_by_id('sum2').send_keys(num2)

    driver.find_element_by_xpath('//*[@id="at-cv-lightbox-button-holder"]/a[2]').click()

    driver.find_element_by_xpath('//*[@id="gettotal"]/button').click()


def close_browser():
    driver.close()


def checkbox_test():
    # todo: code here
    # find the element and click
    check_box = driver.find_element_by_id('isAgeSelected')
    check_box.click()
    # verify the checkbox is checked
    time.sleep(5)
    status = check_box.is_selected()
    print(status)
    # find the message element and get text
    msg = driver.find_element_by_id('txtAge')
    print(f'Final message: {msg.text}')
    assert "Success" in msg.text


def radio_button(gender1):
    gender = gender1.title()
    # inputting values
    if gender == 'Male':
        element = driver.find_element_by_name('optradio')
        element.click()
    elif gender == 'Female':
        element = driver.find_element_by_xpath(
            "//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/label[2]/input[1]")
        element.click()

        # checking if value is selected
        status = element.is_selected()
    print(status)

    # clicking 'getchecked' button
    button = driver.find_element_by_id('buttoncheck')
    button.click()


def input_form_submit(f_name, l_name, email_ad, phone_n, address_h, city1, zip_code,
                      state, website1, hosting_click, p_desc):
    first_name = driver.find_element_by_name('first_name')
    first_name.send_keys(f_name)

    last_name = driver.find_element_by_name('last_name')
    last_name.send_keys(l_name)

    email = driver.find_element_by_name('email')
    email.send_keys(email_ad)

    phone = driver.find_element_by_name('phone')
    phone.send_keys(phone_n)

    address = driver.find_element_by_name('address')
    address.send_keys(address_h)

    city = driver.find_element_by_name('city')
    city.send_keys(city1)

    zipcode = driver.find_element_by_name('zip')
    zipcode.send_keys(zip_code)

    element = driver.find_element_by_name('state')
    drp_state = Select(element)
    drp_state.select_by_visible_text(state)

    website = driver.find_element_by_name('website')
    website.send_keys(website1)

    hosting = hosting_click.title()
    if hosting == 'No':
        driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[10]/div/div[2]/label/input').click()

    elif hosting == 'Yes':
        driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[10]/div/div[1]/label/input').click()

    project_description = driver.find_element_by_name('comment')
    project_description.send_keys(p_desc)

    send_button = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[13]/div/button')
    send_button.click()

    time.sleep(20)
    driver.close()


def ajax_form(name1, description1):
    name = driver.find_element_by_name('title')
    name.send_keys(name1)

    description = driver.find_element_by_xpath("//textarea[@id='description']")
    description.send_keys(description1)

    submit_button = driver.find_element_by_name('btn-submit')
    submit_button.click()


def jquery_select_drp_down(country):
    element = driver.find_element_by_id('country')
    drp_country = Select(element)
    drp_country.select_by_value(country)


def download_file():
    element_download = driver.find_element_by_id('downloadButton')
    element_download.click()


def drag_and_drop():
    actions = ActionChains(driver)

    source_element = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/input[1]")
    target_element = driver.find_element_by_xpath("//output[@id='range']")
    actions.drag_and_drop(source_element, target_element).perform()

    element1_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/div[1]/input[1]")
    element2_target = driver.find_element_by_xpath("//output[@id='rangeSuccess']")
    actions.drag_and_drop(element1_source, element2_target).perform()

    element3_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[3]/div[1]/div[1]/input[1]")
    element3_target = driver.find_element_by_xpath("//output[@id='rangeWarning']")
    actions.drag_and_drop(element3_source, element3_target).perform()

    element4_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[1]/div[2]/div[1]/input[1]")
    element4_target = driver.find_element_by_xpath("//output[@id='rangePrimary']")
    actions.drag_and_drop(element4_source, element4_target)

    element5_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[1]/div[2]/div[1]/input[1]")
    element5_target = driver.find_element_by_xpath("//output[@id='rangePrimary']")
    actions.drag_and_drop(element5_target, element5_source).perform()

    element6_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[2]/div[2]/div[1]/input[1]")
    element6_target = driver.find_element_by_xpath("//output[@id='rangeInfo']")
    actions.drag_and_drop(element6_source, element6_target).perform()

    element7_source = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[2]/section[1]/div[3]/div[2]/div[1]/input[1]")
    element7_target = driver.find_element_by_xpath("//output[@id='rangeDanger']")
    actions.drag_and_drop(element7_source, element7_target).perform()


def explicit_wait_methods():
    url = 'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver'
    driver.get(url)
    # find element and click it
    print('Case 1:')
    element = driver.find_element_by_id('populate-text')
    element.click()
    # text_to_present_in_element(locator,text
    msg_xpath = "//h2[@id='h2']"
    msg_id = 'h2'
    msg_css_selector = '#h2'
    locator1 = (By.XPATH, msg_xpath)
    ext_text = 'Selenium Webdriver'
    wb_wait = WebDriverWait(driver, 60)
    msg = wb_wait.until(EC.text_to_be_present_in_element((By.XPATH, msg_xpath), ext_text))
    print(msg)

    print('Case2')
    display_btn = driver.find_element_by_id('display-other-button')
    display_btn.click()
    print("Wait until enabled button appears:")

    enabled_button = wb_wait.until(EC.visibility_of_element_located((By.ID, 'hidden')))
    enabled_button.click()
    print("Wait until enabled button is disappears:")
    button = wb_wait.until_not(EC.visibility_of_element_located((By.ID, 'hidden')))
    print('Case2 is completed')

    print('Case3')
    display_btn = driver.find_element_by_id('enable-button')
    display_btn.click()
    print("Wait until enabled 'BUTTON' button appears:")

    wb_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#disable')))

    print('Case3 is completed')


