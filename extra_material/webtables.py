from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Python39\chromedriver")

driver.get('https://www.techlistic.com/p/demo-selenium-practice.html')

# copy xpath of header of the table and removed the number so xpath covers all the columns:
rows = len(driver.find_elements_by_xpath(
    '//*[@id="post-body-5867683659713562481"]/div/div/table/thead/tr'))  # counts number of rows

# cop xpath of the first row , then remove the number xpath covers all the rows:
cols = len(driver.find_elements_by_xpath(
    '//*[@id="post-body-5867683659713562481"]/div/div[1]/table/tbody/tr/th'))  # counts number of columns
print(rows)
print(cols)

for i in range(1, cols + 1):
    for c in range(1, rows + 1):
        value = driver.find_elements_by_xpath(
            '//*[@id="post-body-5867683659713562481"]/div/div["+str(i)+"]/table/tbody/tr["+str(c)+"]/th').text
        print(value)
