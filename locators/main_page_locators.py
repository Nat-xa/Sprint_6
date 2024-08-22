from selenium.webdriver.common.by import By


class MainPageLocators:
    # Метод создания локатора для выбора вопроса из списка
    @staticmethod
    def question_by_id(number):
        return By.XPATH, f".//div[@id = 'accordion__heading-{number}']"

    # Метод создания локатора для получения ответа
    @staticmethod
    def answer_by_id(number):
        return By.XPATH, f".//div[@id = 'accordion__panel-{number}']"

    # Кнопка "Заказать" на главной странице сайта
    ORDER_BUTTON_PAGE = [By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]"]
    # Блок "Вопросы о важном" на главной странице сайта
    QUESTION_BLOCK = [By.XPATH, ".//div[@class = 'Home_SubHeader__zwi_E' and text() = 'Вопросы о важном']"]
