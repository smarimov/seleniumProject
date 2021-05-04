import xl_utilities
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")

path = "C:\\Users\\shoki\\OneDrive\\Desktop\\Results.xlsx"

rows = xl_utilities.get_row_count(path, 'Sheet1')

for r in range(2, rows + 1):
    username = xl_utilities.read_data(path, 'Sheet1', r, 1)
    password = xl_utilities.read_data(path, "Sheet1", r, 2)

