"""
This file is going to include methods that will parse
the specific data that we need from each one of the deal boxes.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


class AirbnbReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, "div[class*=c4mnd7m]"
        )

    def pull_deal_box_attributes(self):
        time.sleep(5)
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the property name
            property_name = deal_box.find_element(
                By.CSS_SELECTOR, "div[class*=t1jojoys]"
            ).get_attribute("innerHTML").strip()
            # Pulling the property price
            property_price = deal_box.find_element(
                By.CSS_SELECTOR, "span[class*=_tyxjp1]"
            ).text.strip()
            # Pulling the property score
            property_rating = deal_box.find_element(
                By.CSS_SELECTOR, "span[class*=r1dxllyb]"
            ).get_attribute("innerHTML").strip()

            collection.append(
                [property_name, property_price, property_rating]
            )
        return collection
