import allure
import pytest

import sys 
sys.path.append('..')

from conftest import browser
from pages.logo_page import LogoPage

@pytest.fixture 
def logo_page():
    logo_page=LogoPage()
    return logo_page

class TestButtonLogoPage: # Тестовый класс проверки логотипов на главной странице
    @allure.title("Проверка логотипа 'Яндекс'. ОР - в новом окне откроется главная страница Дзена")
    def test_yandex_button_true(self, browser, logo_page):
        logo_page.open_browser(browser) # Открываем браузер
        logo_page.click_yandex_button(browser) # Нажимаем логотип "Яндекс"
        logo_page.switching_to_the_new_tab(browser) # Переключаемся на новую вкладку
        logo_page.wait_for_page_load(browser) # Ждем загрузки страницы
        logo_page.check_dzen_url(browser) # Проверяем URL "Яндекса"
        # Тест проходит PASSED 

    @allure.title("Проверка логотипа 'Самоката'. ОР - попадем на главную страницу 'Самоката'")
    def test_scooter_button_true(self, browser, logo_page):
        logo_page.open_browser(browser) # Открываем браузер
        logo_page.click_order_button(browser) # Нажатие на кнопку 'Заказать' вверху страницы (смена страницы)
        logo_page.click_scooter_button(browser) # Нажимаем логотип "Самоката"
        logo_page.check_main_page_url(browser) # Проверяем URL "Самоката"
        # Тест проходит PASSED 
