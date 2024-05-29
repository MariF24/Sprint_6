from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import ScootersLocators

class AboutRentTheScooterPageScooter(BasePage):



    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self,url):
       self.navigate(url)
    def enter_delivery_date(self, delivery_date):
        self.enter_text(ScootersLocators.WHEN_TO_BRING_THE_SCOOTER_FIELD, delivery_date)


    def add_rental_period_first(self, rental_date):
        self.click_element(ScootersLocators.RENTAL_PERIOD_FIELD_SELECT)
        self.wait_for_element_visible(ScootersLocators.RENTAL_PERIOD_LIST)
        self.click_element(ScootersLocators.SELECT_RENTAL_PERIOD_FIRST)

    def add_rental_period_second(self, rental_date):
        self.click_element(ScootersLocators.RENTAL_PERIOD_FIELD_SELECT)
        self.wait_for_element_visible(ScootersLocators.RENTAL_PERIOD_LIST)
        self.click_element(ScootersLocators.SELECT_RENTAL_PERIOD_SECOND)

    def click_button_order_placed_in_form(self):
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_IN_FORM)
