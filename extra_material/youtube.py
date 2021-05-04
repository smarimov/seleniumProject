from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")
driver.get('https://www.youtube.com/results?search_query=Shoki%27s+corner')

driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()