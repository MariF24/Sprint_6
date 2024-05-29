
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class HeaderPageScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self,url):
       self.navigate(url)

    def check_link_logo_yandex(self, driver):
        self.click_element(ScootersLocators.LOGO_YANDEX)
        driver.get('https://dzen.ru/?yredirect=true')


    def check_link_logo_scooter(self):
        self.click_element(ScootersLocators.LOGO_SCOOTER)
        self.wait_for_element_visible(ScootersLocators.BUTTON_ORDER_PLACED_HEADER)

    def click_button_order_placed_header(self):
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_HEADER)