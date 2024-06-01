import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class PopupWantToPlacePageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Найти и кликнуть по кнопке Да в модальном окне Хотите оформить заказ?')
    def click_button_yes(self):
        self.click_element(ScootersLocators.BUTTON_YES_WHEN_TO_PLACE_AN_ORDER_FIELD)