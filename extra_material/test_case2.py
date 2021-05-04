import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")
        self.driver.get('https://www.google.com/')
        print(f'Title of the page:{self.driver.title}')

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Program Files\\Python39\\chromedriver")
        self.driver.get('https://www.bing.com/')
        print(f'Title of the page:{self.driver.title}')


if __name__ == "__main__":
    unittest.main()
