"""
This file will include a class with instance methods.
That will be responsible to interact with our website.
After we have some results, to apply filters.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_filters(self):
        time.sleep(2)
        filters_button = self.driver.find_element(
            By.CSS_SELECTOR, "span[class*=t1o11edy]"
        )
        filters_button.click()
        price_range_average = self.driver.find_element(
            By.CSS_SELECTOR, "div[class*=s1kx2c1w]"
        ).text
        print(price_range_average)

    def price_range(self, minprice, maxprice):
        min_price = self.driver.find_element(By.ID, "price_filter_min")
        length_minprice = len(min_price.get_attribute('value'))
        min_price.send_keys(length_minprice * Keys.BACKSPACE)
        min_price.send_keys(minprice)
        max_price = self.driver.find_element(By.ID, "price_filter_max")
        length_maxprice = len(max_price.get_attribute('value'))
        max_price.send_keys(length_maxprice * Keys.BACKSPACE)
        max_price.clear()
        max_price.send_keys(maxprice)
        max_price.send_keys(Keys.TAB)
