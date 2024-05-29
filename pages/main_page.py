from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import ScootersLocators

class MainPageScooter(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self,url):
       self.navigate(url)

    def click_button_confirm_cookie(self):
        self.click_element(ScootersLocators.BUTTON_CONFIRM_COOKIE)


    def check_important_answer_first(self,driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_FIRST)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_FIRST)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_FIRST)


    def check_important_answer_second(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_SECOND)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_SECOND)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_SECOND)

    def check_important_answer_third(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_THIRD)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_THIRD)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_THIRD)

    def check_important_answer_fourth(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_FOURTH)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_FOURTH)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_FOURTH)


    def check_important_answer_fifth(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_FIFTH)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_FIFTH)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_FIFTH)

    def check_important_answer_sixth(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_SIXTH)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_SIXTH)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_SIXTH)

    def check_important_answer_seventh(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_SEVENTH)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_SEVENTH)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_SEVENTH)

    def check_important_answer_eighth(self, driver):
        element = self.find_element(ScootersLocators.IMPORTANT_QUESTION_EIGHTH)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.IMPORTANT_QUESTION_EIGHTH)
        self.wait_for_element_visible(ScootersLocators.IMPORTANT_ANSWER_EIGHTH)

    def click_button_order_placed_middle(self, driver):
        element = self.find_element(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(ScootersLocators.BUTTON_ORDER_PLACED_MIDDLE)