from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')


def e_commerce_search():
    xpath = "//div[@id='block_top_menu']//a[@href='http://automationpractice.com/index.php?id_category=3&controller" \
            "=category'] "
    women_button = driver.find_element_by_xpath(xpath)
    women_button.click()

    women_clothes = driver.find_elements_by_xpath(
        "//ul[@class='product_list grid row']//a[@class='product-name']")

    women_stuff = []

    for cloth in women_clothes:
        women_stuff.append(cloth.text.strip())

    print(len(women_stuff))
    print(women_stuff)


dresses = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')

summer_dresses = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a')

mouse_actions = ActionChains(driver)
mouse_actions.move_to_element(dresses).move_to_element(summer_dresses).click().perform()