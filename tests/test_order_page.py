import allure
import pytest

from data import Urls
from pages.main_page import MainPage
from pages.modal_window_page import ModalWindowPage
from pages.order_page import OrderPage
from settings import OrderSettings, ModalWindowSettings


class TestOrderPage:
    @allure.title('Проверка оформления заказа самоката')
    @pytest.mark.parametrize(OrderSettings.parameters, OrderSettings.value)
    def test_success_order_page_fill_from_header(self, driver, name, family, address,
                                                 station_number, telephone, delivery_day, comment_text):
        main_page = MainPage(driver)
        main_page.open_page(Urls.QA_SCOOTER)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.form_order_fill(name, family, address, station_number, telephone, delivery_day, comment_text)

        modal_window = ModalWindowPage(driver)

        assert (modal_window.open_modal_window(ModalWindowSettings.TEXT_MODAL_WINDOW) ==
                ModalWindowSettings.TEXT_MODAL_WINDOW), 'Текст модального окна не соответствует ожидаемому'

    @allure.title('Проверка работы кнопки "Заказать" в нижней части главной страницы')
    def test_order_button_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.QA_SCOOTER)
        main_page.scroll_and_click_order_button_page()
        order_page = OrderPage(driver)

        assert order_page.get_text_order_header() == OrderSettings.ORDER_HEADER_TEXT

    @allure.title('Проверка перехода на главную страницу при нажатии на логоти "Самокат"')
    def test_logo_scooter_transition(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.QA_SCOOTER)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.click_to_logo_scooter()

        assert (order_page.wait_for_correct_current_url(Urls.QA_SCOOTER)
                == Urls.QA_SCOOTER), 'Ожидаемый URL не соответствует полученному'

    @allure.title('Проверка редиректа на страницу Дзена при нажатии на логотип "Яндекс"')
    def test_logo_yandex_transition(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.QA_SCOOTER)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.click_to_logo_yandex()

        assert order_page.wait_redirect_dzen_and_get_current_url() == Urls.DZEN, \
            'Ожидаемый URL не соответствует полученному'
