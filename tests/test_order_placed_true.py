import pytest
import allure
from selenium import webdriver
from config import URL
from pages.main_page import MainPageScooter
from pages.header_page import HeaderPageScooter
from pages.form_the_scooter_for_page import TheScooterForPageScooter
from pages.form_about_rent_page import AboutRentTheScooterPageScooter
from pages.popup_want_to_place_an_order_page import PopupWantToPlacePageScooter
from pages.popup_order_placed_page import PopupOrderPlacedPageScooter
from locators import ScootersLocators
from data import NAME_FIRST, SURNAME_FIRST, ADDRESS_FIRST, METRO_STATION_FIRST, PHONE_FIRST, DELIVERY_DATE_FIRST, RENTAL_DATE_FIRST, NAME_SECOND, SURNAME_SECOND, ADDRESS_SECOND, METRO_STATION_SECOND, PHONE_SECOND, DELIVERY_DATE_SECOND, RENTAL_DATE_SECOND
class TestOrderButtonHeader:

    @allure.title('Оформление заказа через кнопку Заказать в хедере')
    def test_order_placed_button_header(self, driver):
        main_page = MainPageScooter(driver)
        header_page = HeaderPageScooter(driver)
        form_the_scooter_for_page = TheScooterForPageScooter(driver)
        form_about_rent_page = AboutRentTheScooterPageScooter(driver)
        popup_want_to_place_an_order_page = PopupWantToPlacePageScooter(driver)
        popup_order_placed_page = PopupOrderPlacedPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        header_page.click_button_order_placed_header()
        form_the_scooter_for_page.enter_name(NAME_FIRST)
        form_the_scooter_for_page.enter_surname(SURNAME_FIRST)
        form_the_scooter_for_page.enter_address(ADDRESS_FIRST)
        form_the_scooter_for_page.add_metro_station_first(METRO_STATION_FIRST)
        form_the_scooter_for_page.enter_phone(PHONE_FIRST)
        form_the_scooter_for_page.click_button_further()
        form_about_rent_page.enter_delivery_date(DELIVERY_DATE_FIRST)
        form_about_rent_page.add_rental_period_first(RENTAL_DATE_FIRST)
        form_about_rent_page.click_button_order_placed_in_form()
        popup_want_to_place_an_order_page.click_button_yes()
        popup_order_placed_page.find_order_placed_label()
        header_page.check_link_logo_scooter()
        header_page.check_link_logo_yandex(driver)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Оформление заказа через кнопку Заказать в на главной странице')
    def test_order_placed_button_middle(self, driver):
        main_page = MainPageScooter(driver)
        header_page = HeaderPageScooter(driver)
        form_the_scooter_for_page = TheScooterForPageScooter(driver)
        form_about_rent_page = AboutRentTheScooterPageScooter(driver)
        popup_want_to_place_an_order_page = PopupWantToPlacePageScooter(driver)
        popup_order_placed_page = PopupOrderPlacedPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.click_button_order_placed_middle(driver)
        form_the_scooter_for_page.enter_name(NAME_SECOND)
        form_the_scooter_for_page.enter_surname(SURNAME_SECOND)
        form_the_scooter_for_page.enter_address(ADDRESS_SECOND)
        form_the_scooter_for_page.add_metro_station_second(METRO_STATION_SECOND)
        form_the_scooter_for_page.enter_phone(PHONE_SECOND)
        form_the_scooter_for_page.click_button_further()
        form_about_rent_page.enter_delivery_date(DELIVERY_DATE_SECOND)
        form_about_rent_page.add_rental_period_second(RENTAL_DATE_SECOND)
        form_about_rent_page.click_button_order_placed_in_form()
        popup_want_to_place_an_order_page.click_button_yes()
        popup_order_placed_page.find_order_placed_label()
        header_page.check_link_logo_scooter()
        header_page.check_link_logo_yandex(driver)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'


    @pytest.mark.parametrize('name,surname,address,phone',
    [
        [NAME_FIRST, SURNAME_FIRST, ADDRESS_FIRST, PHONE_FIRST],
        [NAME_SECOND, SURNAME_SECOND, ADDRESS_SECOND, PHONE_SECOND]
    ]
     )

    def test_order_placed_button_middle_with_options(self, name, surname, address, phone, driver):
        main_page = MainPageScooter(driver)
        header_page = HeaderPageScooter(driver)
        form_the_scooter_for_page = TheScooterForPageScooter(driver)
        form_about_rent_page = AboutRentTheScooterPageScooter(driver)
        popup_want_to_place_an_order_page = PopupWantToPlacePageScooter(driver)
        popup_order_placed_page = PopupOrderPlacedPageScooter(driver)
        main_page.open_page(URL)
        main_page.click_button_confirm_cookie()
        main_page.click_button_order_placed_middle(driver)
        form_the_scooter_for_page.enter_name(name)
        form_the_scooter_for_page.enter_surname(surname)
        form_the_scooter_for_page.enter_address(address)
        form_the_scooter_for_page.add_metro_station_second(METRO_STATION_SECOND)
        form_the_scooter_for_page.enter_phone(phone)
        form_the_scooter_for_page.click_button_further()
        form_about_rent_page.enter_delivery_date(DELIVERY_DATE_SECOND)
        form_about_rent_page.add_rental_period_second(RENTAL_DATE_SECOND)
        form_about_rent_page.click_button_order_placed_in_form()
        popup_want_to_place_an_order_page.click_button_yes()
        popup_order_placed_page.find_order_placed_label()
        header_page.check_link_logo_scooter()
        header_page.check_link_logo_yandex(driver)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
