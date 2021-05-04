from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://www.thelevelup.com/')
# Printing number of link on the above website page:
links = driver.find_elements_by_tag_name('a')
print(len(links))

# Printing all the links as text value of the webpage:
for link in links:
    print(link.text)

# How to click on the link
driver.find_element_by_partial_link_text('Case').click()
