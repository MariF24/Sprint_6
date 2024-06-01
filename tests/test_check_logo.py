import pytest
import allure
from selenium import webdriver
from config import URL
from pages.main_page import MainPageScooter
from pages.header_page import HeaderPageScooter
from data import REDIRECT_DZEN
class TestCheckLinkLogo:

    @allure.title('Проверка перехода на главную страницу Самоката при нажатии на лого Самоката')
    def test_check_link_logo_scooter(self, driver):
        main_page = MainPageScooter(driver)
        header_page = HeaderPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        header_page.check_link_logo_scooter()
        assert header_page.get_current_url(URL) == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка редиректа на Дзен при нажатии на лого Яндекс')
    def test_check_link_logo_yandex(self, driver):
        main_page = MainPageScooter(driver)
        header_page = HeaderPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        header_page.check_link_logo_yandex()
        assert header_page.get_current_url(REDIRECT_DZEN) == 'https://dzen.ru/?yredirect=true'