import allure

import sys 
sys.path.append('..')

from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from conftest import browser

class LogoPage:
    
    @allure.step("Открытие браузера")
    def open_browser(self, browser):
        browser.get(URLs.main_page_url)
        return self

    @allure.step("Нажатие на кнопку 'Заказать' вверху страницы ")
    def click_order_button(self, browser):
        browser.find_element(*OrderLocators.order_button_header).click()
        return self

    @allure.step("Нажатие на логотип 'Яндекс'")
    def click_yandex_button(self, browser):
        browser.find_element(*LogoLocators.yandex_button).click()
        return self
    
    @allure.step("Нажатие на логотип 'Самокат'")
    def click_scooter_button(self, browser):
        browser.find_element(*LogoLocators.scooter_button).click()
        return self

    @allure.step("Переключение вкладки")
    def switching_to_the_new_tab(self, browser):
        browser.switch_to.window(browser.window_handles[1])
        return self

    @allure.step("Ожидание загрузки страницы 'Яндекс'")
    def wait_for_page_load(self, browser):
        WebDriverWait(browser, 25).until(EC.visibility_of_element_located(LogoLocators.dzen_logo)) # Ждем загрузки логотипа
        return self

    @allure.step("Проверка URL вкладки 'Дзен'")
    def check_dzen_url(self, browser):
        assert URLs.dzen_url in browser.current_url
        return self

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def check_main_page_url(self, browser):
        assert URLs.main_page_url in browser.current_url
        return self