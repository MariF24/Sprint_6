import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import ScootersLocators
class TheScooterForPageScooter(BasePage):



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Ввести имя')
    def enter_name(self, name):
        self.enter_text(ScootersLocators.NAME_FIELD, name)

    @allure.step('Ввести фамилию')
    def enter_surname(self, surname):
        self.enter_text(ScootersLocators.SURNAME_FIELD, surname)

    @allure.step('Ввести адрес')
    def enter_address(self, address):
        self.enter_text(ScootersLocators.ADDRESS_FIELD, address)

    @allure.step('Добавить станцию метро_вариант №1')
    def add_metro_station_first(self, metro_station):
        self.click_element(ScootersLocators.DROPDOWN_LIST_FOCUS)
        self.wait_for_element_visible(ScootersLocators.DROPDOWN_LIST)
        self.click_element(ScootersLocators.SELECT_STATION_FIRST)

    @allure.step('Добавить станцию метро_вариант №2')
    def add_metro_station_second(self, metro_station):
        self.click_element(ScootersLocators.DROPDOWN_LIST_FOCUS)
        self.wait_for_element_visible(ScootersLocators.DROPDOWN_LIST)
        self.click_element(ScootersLocators.SELECT_STATION_SECOND)

    @allure.step('Ввести телефон')
    def enter_phone(self, phone):
        self.enter_text(ScootersLocators.PHONE_FIELD, phone)

    @allure.step('Нажать на кнопку Далее и подождать появления формы Про аренду')
    def click_button_further(self):
        self.click_element(ScootersLocators.BUTTON_FURTHER)
        self.wait_for_element_visible(ScootersLocators.WHEN_TO_BRING_THE_SCOOTER_FIELD)