from selenium import webdriver

driver = webdriver.Chrome()


def dress_count():
    driver.get('http://automationpractice.com/index.php?id_category=8&controller=category')
    elements = driver.find_elements_by_xpath('//h5[@itemprop="name"]')
    new_list = []
    for element in elements:
        new_list.append(element.text)
    print(new_list)
