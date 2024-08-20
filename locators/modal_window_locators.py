from selenium.webdriver.common.by import By


class ModalWindowLocators:
    # Кнопка "Да" во всплывающем окне
    MODAL_HEADER = [By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']"]