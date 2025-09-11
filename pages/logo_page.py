import allure

import sys 
sys.path.append('..')

from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocators
from pages.base_page import *


class LogoPage(BasePageScooter):
    
    @allure.step("Нажатие на кнопку 'Заказать' вверху страницы ")
    def click_order_button(self):
        self.click_on_element(OrderLocators.order_button_header)
        
    @allure.step("Нажатие на логотип 'Яндекс'")
    def click_yandex_button(self):
        self.click_on_element(LogoLocators.yandex_button)
        self.switching_to_the_new_tab() # Переключение вкладки
        self.wait_for_page_load(LogoLocators.dzen_logo)
        
    @allure.step("Нажатие на логотип 'Самокат'")
    def click_scooter_button(self):
        self.click_on_element(LogoLocators.scooter_button)
