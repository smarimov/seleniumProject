from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
search_box = driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys("Shoki's corner")

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

driver.get('https://ytmp3.cc/youtube-to-mp3/')
