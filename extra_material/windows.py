from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

# First find out the handle value of parent window:
print(driver.current_window_handle)  # CDwindow-DAFF81AD363EB60915CD091BCB42F56C -handle value

# find all handle values for each browsers:
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows": #this closes specific window
        driver.close()

#driver.quit()
