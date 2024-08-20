import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажатие на кнопку "Заказать" в нижней части страницы')
    def click_order_button_page(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_PAGE)
        order_button_page = self.wait_and_find_element(MainPageLocators.ORDER_BUTTON_PAGE)
        order_button_page.click()

    @allure.step('Нажатие на кнопку "Заказать" в шапке страницы')
    def click_order_button_header(self):
        order_button_header = self.wait_and_find_element(BasePageLocators.ORDER_BUTTON_HEADER)
        order_button_header.click()

    @allure.step('Нажатие на вопрос блока "Вопросы о важном"')
    def click_question_number(self, number):
        question_number = self.wait_and_find_element(MainPageLocators.question_by_id(number))
        question_number.click()

    @allure.step('Получение ответа на вопрос блока "Вопросы о важном"')
    def get_question_answer(self, number):
        question_answer = self.wait_and_find_element(MainPageLocators.answer_by_id(number))
        return question_answer.text
