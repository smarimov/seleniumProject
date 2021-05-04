from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scroll down based on pixel numbers

# driver.execute_script("window.scrollBy(0,1000)", "")

# scroll down till we find the element:
#flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
#driver.execute_script("arguments[0].scrollIntoView();", flag)

# scroll to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
