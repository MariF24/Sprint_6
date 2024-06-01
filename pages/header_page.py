import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class HeaderPageScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Получать URL текущей страницы')
    def get_current_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    @allure.step('Найти и кликнуть на лого Яндекс')
    def check_link_logo_yandex(self):
        self.click_element(ScootersLocators.LOGO_YANDEX)

    @allure.step('Найти и кликнуть на лого Самокат, дождаться видимости кнопки Заказать в хедере')
    def check_link_logo_scooter(self):
        self.click_element(ScootersLocators.LOGO_SCOOTER)
        self.wait_for_element_visible(ScootersLocators.BUTTON_ORDER_PLACED_HEADER)

    @allure.step('Найти и кликнуть по кнопке Заказать в хедере')
    def click_button_order_placed_header(self):
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_HEADER)