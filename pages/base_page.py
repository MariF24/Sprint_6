import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    @allure.step('Переходим по URL')
    def navigate(self, url:str):
        self.driver.get(url)

    @allure.step('Находим элемент по локатору')
    def find_element(self, locator:tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    @allure.step('Находим и кликаем на элемент')
    def click_element(self, locator:tuple, timeout: int = 10):
        element = self.find_element(locator,timeout)
        if element:
            element.click()
        else:
            print(f"Failed to click on element with locator {locator}.")

    @allure.step('Находим элемент, очищаем поле ввода и вводим текст')
    def enter_text(self, locator:tuple, text: str, timeout: int = 10):
        element = self.find_element(locator,timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f"Failed to enter text in element with locator {locator}.")

    @allure.step('Проверяем видимость элемента на странице')
    def wait_for_element_visible(self, locator:tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not visible after {timeout} seconds.")
            return None

    @allure.step('Находим элемент посредством скроллинга')
    def scroll_to_element(self, locator:tuple):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element



