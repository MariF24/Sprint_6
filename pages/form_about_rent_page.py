import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import ScootersLocators

class AboutRentTheScooterPageScooter(BasePage):



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Ввести дату доставки самоката')
    def enter_delivery_date(self, delivery_date):
        self.enter_text(ScootersLocators.WHEN_TO_BRING_THE_SCOOTER_FIELD, delivery_date)

    @allure.step('Добавить период аренды_вариант №1')
    def add_rental_period_first(self, rental_date):
        self.click_element(ScootersLocators.RENTAL_PERIOD_FIELD_SELECT)
        self.wait_for_element_visible(ScootersLocators.RENTAL_PERIOD_LIST)
        self.click_element(ScootersLocators.SELECT_RENTAL_PERIOD_FIRST)

    @allure.step('Добавить период аренды_вариант №2')
    def add_rental_period_second(self, rental_date):
        self.click_element(ScootersLocators.RENTAL_PERIOD_FIELD_SELECT)
        self.wait_for_element_visible(ScootersLocators.RENTAL_PERIOD_LIST)
        self.click_element(ScootersLocators.SELECT_RENTAL_PERIOD_SECOND)

    @allure.step('Кликнуть на кнопку Заказать в форме заказа')
    def click_button_order_placed_in_form(self):
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_IN_FORM)
