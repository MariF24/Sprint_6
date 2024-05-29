import pytest
import allure
from selenium import webdriver
from config import URL
from pages.main_page import MainPageScooter
from locators import ScootersLocators
class TestOpenImportantQuestions():

    @allure.title('Проверка первого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_first(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_first(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_FIRST).text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    @allure.title('Проверка второго вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_second(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_second(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_SECOND).text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка третьего вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_third(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_third(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_THIRD).text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка четвертого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_fourth(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_fourth(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_FOURTH).text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка пятого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_fifth(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_fifth(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_FIFTH).text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка шестого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_sixth(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_sixth(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_SIXTH).text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка седьмого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_seventh(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_seventh(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_SEVENTH).text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка восьмого вопроса/ответа в разделе Вопросы о важном')
    def test_check_important_answer_eighth(self, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.check_important_answer_eighth(driver)
        assert driver.find_element(*ScootersLocators.IMPORTANT_ANSWER_EIGHTH).text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

