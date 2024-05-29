from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class PopupOrderPlacedPageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self,url):
       self.navigate(url)

    def find_order_placed_label(self):
        self.find_element(ScootersLocators.ORDER_PLACED_LABEL)
        self.click_element(ScootersLocators.BUTTON_SEE_STATUS)
