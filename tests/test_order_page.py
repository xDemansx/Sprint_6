import allure
import pytest

import sys 
sys.path.append('..')

from pages.base_page import *
from pages.order_page import OrderPage
from data import OrderData
from conftest import driver


class TestOrderPage(): # Тестовый класс проверки позитивного сценария с 2 наборами данных
    @allure.title("Проверка позитивного сценария с 2 наборами данных")
    @pytest.mark.parametrize('number_order', [OrderData.First_Order, OrderData.Second_Order])
    def test_order_positive_true(self, driver, number_order):
        order_page = OrderPage(driver)
        order_page.scroll_to_bottom_order(number_order) # Ищем кнопку 'Заказать'
        order_page.click_to_bottom_order(number_order) # Нажимаем кнопку 'Заказать'
        order_page.filling_user_name(number_order) # Заполняем 'Имя'
        order_page.filling_last_name(number_order) # Заполняем 'Фамилия'
        order_page.filling_address(number_order) # Заполняем 'Адрес'
        order_page.filling_metro(number_order) # Заполняем 'Станцию Метро'
        order_page.filling_user_phone(number_order) # Заполняем 'Номер телефона' и переходим далее
        order_page.click_button_next() # Нажимаем кнопку 'Далее'
        order_page.filling_date_of_delivery(number_order) # Заполняем 'Когда привезти самокат'
        order_page.filling_rental_time(number_order) # Заполняем поле 'Срок аренды'
        order_page.checkbox_colour(number_order) # Выбираем Цвет
        order_page.filling_comment_for_courier(number_order) # Заполняем комментарии
        order_page.click_button_order() # Нажимаем кнопку 'Заказать' в форме 'Про аренду'
        order_page.click_button_yes_in_order() # Нажимаем кнопку 'Да' в форме подтверждения заказа 
        assert order_page.confirmation_window()


