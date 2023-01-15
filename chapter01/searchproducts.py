from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('https://www.baidu.com')

# get the search textbox
search_field = driver.find_element_by_name('wd')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('phones')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
# products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")
products = driver.find_elements_by_xpath("*//div[contains(@class,'c-container') and contains(@class,'xpath-log')]")
products = driver.find_elements_by_xpath("*//div[contains(@class,'c-container') and contains(@class,'xpath-log')]//h3/a")

old_cur_wh = driver.current_window_handle
old_whs = driver.window_handles
print(f'old_cur_window: {old_cur_wh} \n old_windows: {old_whs}')

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print(product.text)
    print(product.get_attribute('href'))
    product.click()
    driver.implicitly_wait(2)
    time.sleep(2)
    
driver.implicitly_wait(20)

# WebDriver will add the new opened windows to the windows list,
# but the current window of webdriver keep not change even the
# new window is opened on the top windows
# so if you want to switch_to.window to what you want,
# 1st. swith to the current shown window window-handands[-1],
# then switch to what you want.you need to switch to the window with the correct window ID

cur_wh = driver.current_window_handle
cur_whs = driver.window_handles
print(f'cur_window: {cur_wh} \n windows: {cur_whs}')
print(f'cur window title {driver.title}-----')
assert cur_wh == old_cur_wh
new_wnds = [wh for wh in cur_whs if wh not in old_whs]
print(new_wnds)

for wh in new_wnds:
    driver.switch_to.window(wh)
    print(f'{driver.current_window_handle},    {driver.title},      {driver.current_url}')
    driver.implicitly_wait(2)
    # driver.refresh()
    time.sleep(3)


# close the browser window
driver.quit()