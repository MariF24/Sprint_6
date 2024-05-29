from selenium.webdriver.common.by import By

class ScootersLocators:
    # Кнопка подтверждения куков
    BUTTON_CONFIRM_COOKIE = [By.ID, 'rcc-confirm-button']
    # Кнопка Заказать на главной странице посередине
    BUTTON_ORDER_PLACED_MIDDLE = [By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[contains(text(),"Заказать")]']
    # Вопрос № 1
    IMPORTANT_QUESTION_FIRST = [By.ID, 'accordion__heading-0']
    # Ответ № 1
    IMPORTANT_ANSWER_FIRST = [By.ID, 'accordion__panel-0']
    # Вопрос № 2
    IMPORTANT_QUESTION_SECOND = [By.ID, 'accordion__heading-1']
    # Ответ № 2
    IMPORTANT_ANSWER_SECOND = [By.ID, 'accordion__panel-1']
    # Вопрос № 3
    IMPORTANT_QUESTION_THIRD = [By.ID, 'accordion__heading-2']
    # Ответ № 3
    IMPORTANT_ANSWER_THIRD = [By.ID, 'accordion__panel-2']
    # Вопрос № 4
    IMPORTANT_QUESTION_FOURTH = [By.ID, 'accordion__heading-3']
    # Ответ № 4
    IMPORTANT_ANSWER_FOURTH = [By.ID, 'accordion__panel-3']
    # Вопрос № 5
    IMPORTANT_QUESTION_FIFTH = [By.ID, 'accordion__heading-4']
    # Ответ № 5
    IMPORTANT_ANSWER_FIFTH = [By.ID, 'accordion__panel-4']
    # Вопрос № 6
    IMPORTANT_QUESTION_SIXTH = [By.ID, 'accordion__heading-5']
    # Ответ № 6
    IMPORTANT_ANSWER_SIXTH = [By.ID, 'accordion__panel-5']
    # Вопрос № 7
    IMPORTANT_QUESTION_SEVENTH = [By.ID, 'accordion__heading-6']
    # Ответ № 7
    IMPORTANT_ANSWER_SEVENTH = [By.ID, 'accordion__panel-6']
    # Вопрос № 8
    IMPORTANT_QUESTION_EIGHTH = [By.ID, 'accordion__heading-7']
    # Ответ № 8
    IMPORTANT_ANSWER_EIGHTH = [By.ID, 'accordion__panel-7']
    # Лого Самокат
    LOGO_SCOOTER = [By.XPATH,'//a[contains(@class,"Header_LogoScooter")]']
    # Лого Яндекс
    LOGO_YANDEX = [By.XPATH, '//a[contains(@href,"//yandex.ru")]']
    # Кнопка Заказать в хедере
    BUTTON_ORDER_PLACED_HEADER = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(text(),"Заказать")]']
    # Модальное окно с информацием о созданном заказе
    ORDER_PLACED_LABEL = [By.XPATH, '//div[contains(@class, "Order_ModalHeader")]']
    # Кнопка Да в модальном окне Хотите оформить заказ?
    BUTTON_YES_WHEN_TO_PLACE_AN_ORDER_FIELD = [By.XPATH, '//button[contains(@class, "Button_Middle") and (text() ="Да")]']
    # Поле Когда привезти самокат
    WHEN_TO_BRING_THE_SCOOTER_FIELD = [By.XPATH, '//input[contains(@placeholder,"* Когда привезти самокат")]']
    # Открытое поле периода аренды
    RENTAL_PERIOD_FIELD_SELECT = [By.XPATH, '//span[(@class = "Dropdown-arrow")]']
    # Выбранное поле с перечнем периодов аренды
    RENTAL_PERIOD_LIST = [By.XPATH, '//div[(@class = "Dropdown-menu")]']
    # Выбор аренды на сутки
    SELECT_RENTAL_PERIOD_FIRST = [By.XPATH, '//div[(@class = "Dropdown-option" and text() = "сутки")]']
    # Выбор аренды на трое суток
    SELECT_RENTAL_PERIOD_SECOND = [By.XPATH, '//div[(@class = "Dropdown-option" and text() = "трое суток")]']
    # Кнопка Заказать в форме заказа
    BUTTON_ORDER_PLACED_IN_FORM = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[contains(text(),"Заказать")]']
    # Поле Имя
    NAME_FIELD = [By.XPATH, '//input[contains(@placeholder,"* Имя")]']
    # Поле Фамилия
    SURNAME_FIELD = [By.XPATH, '//input[contains(@placeholder,"* Фамилия")]']
    # Поле Адрес
    ADDRESS_FIELD = [By.XPATH, '//input[contains(@placeholder,"* Адрес: куда привезти заказ")]']
    # Фокус на поле со списком станций метро
    DROPDOWN_LIST_FOCUS = [By.XPATH, '//input[contains(@class,"select-search__input")]']
    # Выбранное поле с перечнем станций метро
    DROPDOWN_LIST = [By.XPATH, '//div[contains(@class,"select-search__select")]']
    # Выбор станции метро Черкизовская
    SELECT_STATION_FIRST = [By.XPATH, '//li[(@class = "select-search__row" and @data-index = "1" and @data-value="2")]']
    # Выбор станции метро Лубянка
    SELECT_STATION_SECOND = [By.XPATH, '//li[(@class = "select-search__row" and @data-index = "3" and @data-value="4")]']
    # Поле Телефон
    PHONE_FIELD = [By.XPATH, '//input[contains(@placeholder,"* Телефон: на него позвонит курьер")]']
    # Кнопка Далее
    BUTTON_FURTHER = [By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[contains(text(),"Далее")]']
    # Кнопка Посмотреть статус
    BUTTON_SEE_STATUS = [By.XPATH, '//button[contains(text(),"Посмотреть статус")]']

