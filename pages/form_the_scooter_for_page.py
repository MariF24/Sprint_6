from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import ScootersLocators
class TheScooterForPageScooter(BasePage):



    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self,url):
       self.navigate(url)

    def enter_name(self, name):
        self.enter_text(ScootersLocators.NAME_FIELD, name)

    def enter_surname(self, surname):
        self.enter_text(ScootersLocators.SURNAME_FIELD, surname)

    def enter_address(self, address):
        self.enter_text(ScootersLocators.ADDRESS_FIELD, address)

    def add_metro_station_first(self, metro_station):
        self.click_element(ScootersLocators.DROPDOWN_LIST_FOCUS)
        self.wait_for_element_visible(ScootersLocators.DROPDOWN_LIST)
        self.click_element(ScootersLocators.SELECT_STATION_FIRST)
    def add_metro_station_second(self, metro_station):
        self.click_element(ScootersLocators.DROPDOWN_LIST_FOCUS)
        self.wait_for_element_visible(ScootersLocators.DROPDOWN_LIST)
        self.click_element(ScootersLocators.SELECT_STATION_SECOND)


    def enter_phone(self, phone):
        self.enter_text(ScootersLocators.PHONE_FIELD, phone)
    def click_button_further(self):
        self.click_element(ScootersLocators.BUTTON_FURTHER)
        self.wait_for_element_visible(ScootersLocators.WHEN_TO_BRING_THE_SCOOTER_FIELD)