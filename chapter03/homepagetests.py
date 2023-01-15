import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_text_field_max_length(self):
        # get the search textbox
        search_field = self.driver.find_element_by_id('search')

        # check maxlength attribute is set to 128
        self.assertEqual('128', search_field.get_attribute('maxlength'))

    def test_search_button_enabled(self):
        # get Search button
        search_button = self.driver.find_element_by_class_name('button')

        # check Search button is enabled
        self.assertTrue(search_button.is_enabled())

    def test_my_account_link_is_displayed(self):
        # get the Account link
        account_link = self.driver.find_element_by_link_text('ACCOUNT')

        # check My Account link is displayed/visible in the Home page footer
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get the all the links with Account text in it
        account_links = self.driver.\
            find_elements_by_partial_link_text('ACCOUNT')

        # check Account and My Account link is displayed/visible in the Home page footer
        self.assertTrue(len(account_links), 2)

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element_by_class_name('promos')

        # get images from the banner_list
        banners = banner_list.find_elements_by_tag_name('img')

        # check there are 3 banners displayed on the page
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        # get vip promo image
        vip_promo = self.driver.\
            find_element_by_xpath("//img[@alt='Shop Private Sales - Members Only']")

        # check vip promo logo is displayed on home page
        self.assertTrue(vip_promo.is_displayed())
        # click on vip promo images to open the page
        vip_promo.click()
        # check page title
        self.assertEqual("VIP", self.driver.title)

    def test_shopping_cart_status(self):
        # check content of My Shopping Cart block on Home page
        # get the Shopping cart icon and click to open the Shopping Cart section
        shopping_cart_icon = self.driver.\
            find_element_by_css_selector('div.header-minicart span.icon')
        shopping_cart_icon.click()

        # get the shopping cart status
        shopping_cart_status = self.driver.\
            find_element_by_css_selector('p.empty').text
        self.assertEqual('You have no items in your shopping cart.',
                          shopping_cart_status)
        # close the shopping cart section
        close_button = self.driver.\
            find_element_by_css_selector('div.minicart-wrapper a.close')
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


class mypagetest(unittest.TestCase):
    # _url = "file:///C:/Pystudy/learnsewithpython/chapter03/mypage.html"
    _url = "https://cn.bing.com"

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = cls._url
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(30)
        cls.driver.get(cls.url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        pass

    # find_element_by_id
    # <div id="est_cn" class="est_common est_selected">国内版</div>
    def test_01_by_id(self):
        button_element = self.driver.find_element_by_id('est_cn')
        print(button_element.text) #button_element.text = 国内版
        self.assertEqual(button_element.text, "国内版")

    # find_element_by_class_name
    # <div id="est_cn" class="est_common est_selected">国内版</div>
    # there are two classes for div id='est_cn', both can be used to find the tag.
    # but those class names cannot be used together for find_element
    def test_02_by_class_name(self):
        try:
            button_element = self.driver.find_element_by_class_name('est_common est_selected')
        except Exception as e:
            print(f'there is a error { {e} }')
        else:
            print(button_element.text, button_element.tag_name)
            self.assertTrue(False, "something is wrong")
        # correct ones
        button_element = self.driver.find_element_by_class_name('est_common')
        print(button_element.text, button_element.tag_name) #button_element.text = 国内版
        self.assertEqual(button_element.text, "国内版")
        # or
        button_element = self.driver.find_element_by_class_name('est_selected')
        print(button_element.text, button_element.tag_name)  # button_element.text = 国内版
        self.assertEqual(button_element.text, "国内版")

    # find_element_by_xpath
    # <div id="est_cn" class="est_common est_selected">国内版</div>
    def test_03_by_xpath(self):
        button_element = self.driver.find_element_by_xpath('//*[@id="est_cn"]')  # xpath
        print(button_element.text, button_element.tag_name)  # button_element.text = 国内版
        self.assertEqual(button_element.text, "国内版")
        # or
        button_element = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div/div[1]')  # full xpath
        print(button_element.text, button_element.tag_name)  # button_element.text = 国内版
        self.assertEqual(button_element.text, "国内版")

    # find_element_by_name
    # <input id="sb_form_go" type="submit" aria-label="Search" name="search" value="" tabindex="0" data-bm="11">
    def test_04_by_name(self):
        input_element = self.driver.find_element_by_name('search')
        print(input_element.tag_name)  # input_element.text = input
        self.assertEqual(input_element.get_attribute('type'), "submit")  # attribute is for HTML, here attribute('type') = 'submit'

    # find_element_by_tag_name
    # <form data-h="ID=HpApp,21474.1" class="sb_form hassbi hasmic" id="sb_form" action="/search" aria-live="polite" aria-expanded="false"><div i....
    def test_05_by_tag_name(self):
        form_element = self.driver.find_element_by_tag_name('form')
        print(form_element.get_attribute('id'), form_element.get_attribute('data-h'))
        self.assertEqual(self._url+'/search', form_element.get_attribute('action'))

    # fine_element_by_css_selector
    # <div id="est_cn" class="est_common est_selected">国内版</div>
    def test_06_by_css_selector(self):
        button_element1 = self.driver.find_element_by_css_selector("#est_switch .est_selected")
        button_element2 = self.driver.find_element_by_css_selector("#est_switch .est_common")
        self.assertEqual(button_element1, button_element2)

        button_element3 = self.driver.find_element_by_css_selector(".est_common.est_selected")
        print(button_element3.text)
        self.assertEqual(button_element3.text, "国内版")

    # find element by link text
    # <a href="/images?FORM=Z9LH" data-h="ID=HpApp,9107.1" target="" rel="noopener" class="">图片</a>
    def test07_by_link_text(self):
        link_element = self.driver.find_element_by_link_text('图片')
        print(link_element.text, 'link: ', link_element.tag_name, link_element.get_attribute('href'), sep='        ')
        self.assertEqual(link_element.text, '图片')

    # find element by partial link text
    # <a href="/images?FORM=Z9LH" data-h="ID=HpApp,9107.1" target="" rel="noopener" class="">图片</a>
    def test08_by_partial_link_text(self):
        link_element = self.driver.find_element_by_partial_link_text('图')
        print(link_element.text, 'link: ', link_element.tag_name, link_element.get_attribute('href'), sep='        ')
        self.assertEqual(link_element.text, '图片')


    # find element ( by....)
    # <a href="/images?FORM=Z9LH" data-h="ID=HpApp,9107.1" target="" rel="noopener" class="">图片</a>
    def test09_find_element(self):
        link_element = self.driver.find_element(By.LINK_TEXT, '图片')
        print(link_element.text, link_element.get_attribute('href'), sep=',     ')
        self.assertEqual(link_element.text,'图片')

if __name__ == '__main__':
    unittest.main(verbosity=2)

