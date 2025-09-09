from selenium.webdriver.common.by import By 

import sys 
sys.path.append('..')


# Локаторы ЗАКАЗА!
class OrderLocators: 
    # Кнопка "Заказать"
    order_button_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]') # Кнопка "Заказать" вверху страницы
    order_button_centre = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]') # Кнопка "Заказать" внизу страницы

    # Данные пользователя - Окно "Для кого самокат"
    name = (By.XPATH, '//input[@placeholder="* Имя"]')
    last_name = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    list_station = (By.XPATH, "//li[@data-index='0']") 
    number = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//button[contains(text(), "Далее")]')

    # Данные аренды - Окно "Про аренду"
    delivery_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    renta_date = (By.XPATH, '//span[@class = "Dropdown-arrow"]') # локатор поля Срок аренды
    renta_long = [(By.XPATH, '//div[text()="пятеро суток"]'), # локаторы вариантов Срока аренды
                (By.XPATH, '//div[text()="сутки"]')]

    colour_black = (By.XPATH, '//label[@for="black"]')
    colour_grey = (By.XPATH, '//label[@for="grey"]')
    comments = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')

    # Кнопка "Да" - Окно "Хотите оформить заказ?"
    yes_button = (By.XPATH, '//button[text()="Да"]')

    # Текст - Окно "Заказ оформлен"
    order_created = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
