import allure

from locators.modal_window_locators import ModalWindowLocators
from pages.base_page import BasePage


class ModalWindowPage(BasePage):
    @allure.step('Открытие модального окна после заполнения формы заказа')
    def open_modal_window(self, modal_header):
        modal_window = self.wait_text_and_find_element(ModalWindowLocators.MODAL_HEADER, modal_header)
        return modal_window.text
