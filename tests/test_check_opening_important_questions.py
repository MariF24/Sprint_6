import pytest
import allure
from selenium import webdriver
from config import URL
from pages.main_page import MainPageScooter
from locators import ScootersLocators
class TestOpenImportantQuestions():


    text_answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    text_answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    text_answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    text_answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    text_answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    text_answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    locator_q_1 = ScootersLocators.IMPORTANT_QUESTION_FIRST
    locator_a_1 = ScootersLocators.IMPORTANT_ANSWER_FIRST
    locator_q_2 = ScootersLocators.IMPORTANT_QUESTION_SECOND
    locator_a_2 = ScootersLocators.IMPORTANT_ANSWER_SECOND
    locator_q_3 = ScootersLocators.IMPORTANT_QUESTION_THIRD
    locator_a_3 = ScootersLocators.IMPORTANT_ANSWER_THIRD
    locator_q_4 = ScootersLocators.IMPORTANT_QUESTION_FOURTH
    locator_a_4 = ScootersLocators.IMPORTANT_ANSWER_FOURTH
    locator_q_5 = ScootersLocators.IMPORTANT_QUESTION_FIFTH
    locator_a_5 = ScootersLocators.IMPORTANT_ANSWER_FIFTH
    locator_q_6 = ScootersLocators.IMPORTANT_QUESTION_SIXTH
    locator_a_6 = ScootersLocators.IMPORTANT_ANSWER_SIXTH
    locator_q_7 = ScootersLocators.IMPORTANT_QUESTION_SEVENTH
    locator_a_7 = ScootersLocators.IMPORTANT_ANSWER_SEVENTH
    locator_q_8 = ScootersLocators.IMPORTANT_QUESTION_EIGHTH
    locator_a_8 = ScootersLocators.IMPORTANT_ANSWER_EIGHTH
    @pytest.mark.parametrize('locator_question,locator_answer,text_answer',
    [
        [locator_q_1, locator_a_1, text_answer_1],
        [locator_q_2, locator_a_2, text_answer_2],
        [locator_q_3, locator_a_3, text_answer_3],
        [locator_q_4, locator_a_4, text_answer_4],
        [locator_q_5, locator_a_5, text_answer_5],
        [locator_q_6, locator_a_6, text_answer_6],
        [locator_q_7, locator_a_7, text_answer_7],
        [locator_q_8, locator_a_8, text_answer_8]
    ]
                             )
    @allure.title('Проверка соответствия вопросов/ответов в разделе Вопросы о важном')
    def test_check_important(self, locator_question, locator_answer, text_answer, driver):
        main_page = MainPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.click_important_question(locator_question)
        assert main_page.get_text_important_answer(locator_answer) == text_answer



