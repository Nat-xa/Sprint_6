from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Метод создания локатора для выбора станции метро
    @staticmethod
    def metro_station_by_value(station_number):
        return By.XPATH, f".//button[@value = {station_number}]"

    # Метод создания локатора для выбора даты доставки самоката
    @staticmethod
    def delivery_time_by_day(delivery_day):
        return By.XPATH, f".//div[contains(@aria-label, '{delivery_day}-е августа 2024 г.')]"

    # Поле "Имя" в форме заказа самоката
    NAME_FIELD = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    # Поле "Фамилия" в форме заказа самоката
    FAMILY_FIELD = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    # Поле "Адрес: куда привезти заказ" в форме заказа самоката
    ADDRESS_FIELD = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    # Поле "Станция метро" в форме заказа самоката
    METRO_STATION_FIELD = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    # Поле "Телефон: на него позвонит курьер" в форме заказа самоката
    TELEPHONE_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    # Кнопка "Далее" на странице заказа самоката
    NEXT_BUTTON = [By.XPATH, ".//button[text() = 'Далее']"]
    # Поле "Когда привезти самокат" в форме заказа самоката
    DELIVERY_TIME = [By.XPATH, ".// input[@placeholder = '* Когда привезти самокат']"]
    # Поле "Срок аренды" в форме заказа самоката
    RENTAL_PERIOD = [By.XPATH, ".//div[@class = 'Dropdown-placeholder']"]
    # Выпадающий список поля "Срок аренды" (выбор варианта "двое суток")
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, ".//div[text() = 'двое суток']"]
    # Поле "Цвет самоката" в форме заказа самоката (выбор значения "серая безысходность").
    COLOR = [By.XPATH, ".//input[@id = 'grey']"]
    # Поле "Комментарий для курьера" в форме заказа самоката
    COMMENT = [By.XPATH, ".// input[@placeholder = 'Комментарий для курьера']"]
    # Кнопка "Заказать" в форме заказа самоката
    ORDER_BUTTON_FORM_ORDER = [By.XPATH, ".//div[@class = 'Order_Content__bmtHS']//button[text() = 'Заказать']"]
    # Заголовок формы заказа
    ORDER_HEADER = [By.XPATH, ".//div[@class = 'Order_Header__BZXOb']"]
