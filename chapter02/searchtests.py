import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('https://www.baidu.com/')

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        # products = self.driver\
            # .find_elements_by_xpath("//h2[@class='product-name']/a")
        products = self.driver \
            .find_elements_by_xpath("*//div[contains(@class,'c-container') and contains(@class,'xpath-log')]//h3/a")
        self.assertEqual(10, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('salt shaker')
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        # products = self.driver.\
        #     find_elements_by_xpath("//h2[@class='product-name']/a")
        products = self.driver. \
            find_elements_by_xpath("*//div[contains(@class,'c-container') and contains(@class,'xpath-log')]//h3/a")
        self.assertEqual(1, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
