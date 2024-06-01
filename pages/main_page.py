import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class MainPageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Mozila')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Найти и кликнуть по кнопке с подтверждением кук')
    def click_button_confirm_cookie(self):
        self.click_element(ScootersLocators.BUTTON_CONFIRM_COOKIE)

    @allure.step('Найти вопрос из перечня важных вопросов через скроллинг и кликнуть на него')
    def click_important_question(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_element_visible(locator)
        self.click_element(locator)
        self.wait_for_element_visible(locator)

    @allure.step('Найти ответ из перечня ответов и получить его текст')
    def get_text_important_answer(self, locator):
        element = self.find_element(locator).text
        return element

    @allure.step('Кликнуть на кнопку Заказать в середине главной страницы')
    def click_button_order_placed_middle(self):
        self.scroll_to_element(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)
        self.wait_for_element_visible(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)
        self.wait_for_element_visible(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)

