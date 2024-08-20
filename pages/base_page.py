import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента на странице')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента на странице с конкретным текстом')
    def wait_text_and_find_element(self, locator, text):
        WebDriverWait(self.driver, 20).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание появления URL')
    def wait_for_correct_current_url(self, desired_url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(desired_url))
        return self.driver.current_url

    @allure.step('Ожидание изменения URL на Дзен и получение актуального URL')
    def wait_redirect_dzen_and_get_current_url(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))
        return self.driver.current_url

    @allure.step('Нажатие на логотип "Самокат"')
    def click_to_logo_scooter(self):
        logo_scooter_img = self.wait_and_find_element(BasePageLocators.LOGO_SCOOTER)
        logo_scooter_img.click()

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_to_logo_yandex(self):
        logo_yandex_img = self.wait_and_find_element(BasePageLocators.LOGO_YANDEX)
        logo_yandex_img.click()
