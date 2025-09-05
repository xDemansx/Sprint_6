import allure
import pytest

import sys 
sys.path.append('..')

from data import OrderData
from conftest import browser
from pages.order_page import OrderPage

class TestOrderPage(): # Тестовый класс проверки позитивного сценария с 2 наборами данных
    @allure.title("Проверка позитивного сценария с 2 наборами данных")
    @pytest.mark.parametrize('click_order_button, number_order', [('click_first_button', OrderData.First_Order), # "Нажатие по кнопке 'Заказать' вверху страницы"
                                                                  ('click_second_button', OrderData.Second_Order)]) # "Нажатие по кнопке 'Заказать' внизу страницы"
                        
    def test_order_positive_true(self, browser, click_order_button, number_order):
        order_page=OrderPage()

        order_page.open_browser(browser) # Открываем браузер 
        getattr(order_page, click_order_button)(browser) # Нужно выбрать одну из переданных вариантов кнопки Заказать и нажать на неё
        order_page.user_rent_order(browser, **number_order) # Передаем все данные для заказа (при использовании ** в объявлении функции, она соберёт все переданные именованные аргументы в словарь)
        # Тесты проходят PASSED. Оба заказа выполняются с правильными данными.