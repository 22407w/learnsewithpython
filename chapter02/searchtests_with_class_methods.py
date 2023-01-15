import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://www.baidu.com/')

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.\
            find_elements_by_xpath("//div[contains(@class,'c-container') and contains(@class,'xpath-log')]//h3/a")
        self.assertEqual(3, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('salt shaker')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.\
            find_elements_by_xpath("//div[contains(@class,'c-container') and contains(@class,'xpath-log')]//h3/a")
        self.assertEqual(10, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
