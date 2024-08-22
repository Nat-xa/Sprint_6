from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопка "Заказать" в шапке сайта
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    # Логотип "Самокат"
    LOGO_SCOOTER = [By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']"]
    # Логотип "Яндекс"
    LOGO_YANDEX = [By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']"]
