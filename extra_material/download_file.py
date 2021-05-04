from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=C:/Desktop")

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://demo.automationtesting.in/FileDownload.html')

# How to download a text file
driver.find_element_by_id('textbox').send_keys('testing')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()

# How to download pdf file
driver.find_element_by_id('pdfbox').send_keys('Hi Shoki')
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()
