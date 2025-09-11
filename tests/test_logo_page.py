import allure
import pytest

import sys
sys.path.append('..')

from conftest import driver
from pages.base_page import *
from pages.logo_page import LogoPage


class TestButtonLogoPage: # Тестовый класс проверки логотипов на главной странице
    @allure.title("Проверка логотипа 'Яндекс'. ОР - в новом окне откроется главная страница Дзена")
    def test_yandex_button_true(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_yandex_button() # Нажимаем логотип "Яндекс"
        assert logo_page.check_dzen_url() # Проверяем URL "Яндекса"
        # Тест проходит PASSED         


    @allure.title("Проверка логотипа 'Самоката'. ОР - попадем на главную страницу 'Самоката'")
    def test_scooter_button_true(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_order_button() # Нажатие на кнопку 'Заказать' вверху страницы (смена страницы)
        logo_page.click_scooter_button() # Нажимаем логотип "Самоката"
        assert logo_page.check_main_page_url() # Проверяем URL "Самоката"
        # Тест проходит PASSED 
