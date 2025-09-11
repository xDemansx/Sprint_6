import allure

import sys 
sys.path.append('..')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from conftest import driver


class BasePageScooter:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver
        driver.get(URLs.main_page_url) # Открытие главной страницы

    @allure.step("Ожидание загрузки элемента")
    def wait_for_page_load(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    @allure.step("Переключение вкладки")
    def switching_to_the_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
      
    @allure.step("Ищем элемент")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
    @allure.step("Нажатие на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()
    
    @allure.step("Заполнение поля")
    def set_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Проверка URL вкладки 'Дзен'")
    def check_dzen_url(self):
        return URLs.dzen_url in self.driver.current_url
        
    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def check_main_page_url(self):
        return URLs.main_page_url in self.driver.current_url
        