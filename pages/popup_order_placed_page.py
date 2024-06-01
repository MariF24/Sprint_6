import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class PopupOrderPlacedPageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Находим модальное окно с информацией о созданном заказе')
    def find_order_placed_label(self):
        self.find_element(ScootersLocators.ORDER_PLACED_LABEL)

    @allure.step('Найти кнопку Получить статус и получаем ее текст')
    def get_button_see_status_text(self):
        element = self.find_element(ScootersLocators.BUTTON_SEE_STATUS).text
        return element

