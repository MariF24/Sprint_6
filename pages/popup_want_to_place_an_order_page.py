from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class PopupWantToPlacePageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self,url):
       self.navigate(url)

    def click_button_yes(self):
        self.click_element(ScootersLocators.BUTTON_YES_WHEN_TO_PLACE_AN_ORDER_FIELD)