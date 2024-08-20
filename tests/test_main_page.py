import allure
import pytest

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from settings import QuestionSettings


class TestMainPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('В рамках теста проверяется работа выпадающего списка, получение ответа на каждый вопрос,'
                        'соответствие полученных ответов тексту')
    @pytest.mark.parametrize(QuestionSettings.param, QuestionSettings.value)
    def test_faq(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.QA_SCOOTER)
        main_page.scroll_to_element(MainPageLocators.QUESTION_BLOCK)
        main_page.wait_and_find_element(MainPageLocators.QUESTION_BLOCK)
        main_page.click_question_number(number)

        assert main_page.get_question_answer(number) == expected_answer
