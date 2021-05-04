import time

from source.selenium_source import *

driver.get('https://www.seleniumeasy.com/test/drag-and-drop-demo.html')
drag1 = driver.find_element_by_xpath("//span[contains(text(),'Draggable 2')]")
time.sleep(2)
drop_location = driver.find_element_by_xpath('//div[@dropzone="move"]')


actions = ActionChains(driver)
actions.drag_and_drop(drag1, drop_location).perform()
