import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def set_name_input(self, name):
        name_input = self.wait_and_find_element(OrderPageLocators.NAME_FIELD)
        name_input.send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_family_input(self, family):
        family_input = self.wait_and_find_element(OrderPageLocators.FAMILY_FIELD)
        family_input.send_keys(family)

    @allure.step('Заполнение поля "Адрес: куда привезти заказ"')
    def set_address_input(self, address):
        address_input = self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD)
        address_input.send_keys(address)

    @allure.step('Заполнение поля "Станция метро"')
    def set_metro_station_input(self, station_number):
        metro_station_input = self.wait_and_find_element(OrderPageLocators.METRO_STATION_FIELD)
        metro_station_input.click()
        metro_station_value = self.wait_and_find_element(OrderPageLocators.metro_station_by_value(station_number))
        metro_station_value.click()

    @allure.step('Заполнение поля "Телефон: на него позвонит курьер"')
    def set_telephone_number(self, telephone):
        telephone_number_input = self.wait_and_find_element(OrderPageLocators.TELEPHONE_NUMBER_FIELD)
        telephone_number_input.send_keys(telephone)

    @allure.step('Нажатие на кнопку "Далее" в форме заказа самоката')
    def click_next_button(self):
        next_button = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()

    @allure.step('Заполнение поля "Когда привезти самокат"')
    def set_delivery_time(self, delivery_day):
        delivery_time_input = self.wait_and_find_element(OrderPageLocators.DELIVERY_TIME)
        delivery_time_input.click()
        delivery_time = self.wait_and_find_element(OrderPageLocators.delivery_time_by_day(delivery_day))
        delivery_time.click()

    @allure.step('Заполнение поля "Срок аренды"')
    def set_rental_period(self):
        rental_period_input = self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD)
        rental_period_input.click()
        rental_period_dropdown = self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_dropdown.click()

    @allure.step('Заполнение поля выбора цвета самоката')
    def set_scooter_color(self):
        scooter_color_input = self.wait_and_find_element(OrderPageLocators.COLOR)
        scooter_color_input.click()

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_comment(self, comment):
        comment_input = self.wait_and_find_element(OrderPageLocators.COMMENT)
        comment_input.send_keys(comment)

    @allure.step('Нажатие на кнопку "Заказать" в форме заказа самоката')
    def click_order_button_form_order(self):
        order_button = self.wait_and_find_element(OrderPageLocators.ORDER_BUTTON_FORM_ORDER)
        order_button.click()

    @allure.step('Ожидание заголовка формы заказа и получение его текста')
    def get_text_order_header(self):
        text_order_header = self.wait_and_find_element(OrderPageLocators.ORDER_HEADER)
        return text_order_header.text

    @allure.step('Заполнение формы заказа самоката')
    def form_order_fill(self, name, family, address, station_number, telephone, delivery_day, comment):
        self.set_name_input(name)
        self.set_family_input(family)
        self.set_address_input(address)
        self.set_metro_station_input(station_number)
        self.set_telephone_number(telephone)
        self.click_next_button()
        self.set_delivery_time(delivery_day)
        self.set_rental_period()
        self.set_scooter_color()
        self.set_comment(comment)
        self.click_order_button_form_order()
