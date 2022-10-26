from airbnb import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from airbnb.filters import Filters
from airbnb.airbnb_report import AirbnbReport
from prettytable import PrettyTable


class Airbnb(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument('--headless')
        super(Airbnb, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.URL_BASE)

    def select_language(self, language):
        change_language_button = self.find_element(
            By.CLASS_NAME, "_1ubw29"
        )
        change_language_button.click()
        languages_button = self.find_element(
            By.CSS_SELECTOR, f"a[lang={language}]"
        )
        languages_button.click()

    def cookies_permission(self):
        accept_cookies_button = self.find_element(
            By.CLASS_NAME, "_148dgdpk"
        )
        accept_cookies_button.click()

    def select_parameters(self, region, checkin, checkout, adults, children, infants, pets):
        open_fields_button = self.find_element(By.CSS_SELECTOR, "div[class*=s1qcpybl]")
        open_fields_button.click()
        where_button = self.find_element(By.CSS_SELECTOR, "label[class*=in3kizz]")
        where_button.click()
        select_region_button = self.find_element(
            By.XPATH, f'//*[@id="locationInspirationsSectionID"]/div/div[{region}]/div/button'
        )
        select_region_button.click()
        check_in = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{checkin}"]')
        check_in.click()
        check_out = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{checkout}"]')
        check_out.click()
        who_button = self.find_element(
            By.CSS_SELECTOR, "div[data-testid=structured-search-input-field-guests-button]"
        )
        who_button.click()
        # Adults
        for adults in range(adults):
            adults_increase_button = self.find_element(
                By.CSS_SELECTOR, "button[data-testid=stepper-adults-increase-button]"
            )
            adults_increase_button.click()
            adults_value = self.find_element(
                By.CSS_SELECTOR, "span[data-testid=stepper-adults-value]"
            )
            number_of_adults = adults_value.text
            if number_of_adults == adults:
                break
        # Children
        for children in range(children):
            children_increase_button = self.find_element(
                By.CSS_SELECTOR, "button[data-testid=stepper-children-increase-button]"
            )
            children_increase_button.click()
            children_value = self.find_element(
                By.CSS_SELECTOR, "span[data-testid=stepper-children-value]"
            )
            number_of_children = children_value.text
            if number_of_children == children:
                break
        # Infants
        for infants in range(infants):
            infants_increase_button = self.find_element(
                By.CSS_SELECTOR, "button[data-testid=stepper-infants-increase-button]"
            )
            infants_increase_button.click()
            infants_value = self.find_element(
                By.CSS_SELECTOR, "span[data-testid=stepper-infants-value]"
            )
            number_of_infants = infants_value.text
            if number_of_infants == infants:
                break
        # Pets
        for pets in range(pets):
            pets_increase_button = self.find_element(
                By.CSS_SELECTOR, "button[data-testid=stepper-pets-increase-button]"
            )
            pets_increase_button.click()
            pets_value = self.find_element(
                By.CSS_SELECTOR, "span[data-testid=stepper-pets-value]"
            )
            number_of_pets = pets_value.text
            if number_of_pets == pets:
                break

    def search_for(self):
        search_button = self.find_element(By.CLASS_NAME, "_jxxpcd")
        search_button.click()

    def apply_filters(self, minprice, maxprice):
        filters = Filters(driver=self)
        filters.select_filters()
        filters.price_range(minprice, maxprice)

    def property_type(self, *properties):
        property_type_box = self.find_element(
            By.CLASS_NAME, "_19dpbcv"
        )
        property_child_elements = property_type_box.find_elements(
            By.CLASS_NAME, '_1doy7q3'
        )
        for property in properties:
            for property_type_element in property_child_elements:
                if property_type_element.text.strip() == f'{property}':
                    property_type_element.click()
        confirm_button = self.find_element(By.CLASS_NAME, "_1ku51f04")
        confirm_button.click()

    def report_results(self):
        result = self.find_element(
            By.CSS_SELECTOR, "div[class*=gh7uyir]"
        )
        report = AirbnbReport(result)
        table = PrettyTable(
            field_names=["Property Name", "Price per night", "Rating"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
