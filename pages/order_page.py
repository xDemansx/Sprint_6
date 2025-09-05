import allure

import sys 
sys.path.append('..')

from data import URLs
from conftest import browser
from locators.order_locators import OrderLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Шаги заказа
class OrderPage: 

    @allure.step("Открытие браузера")
    def open_browser(self, browser):
        browser.get(URLs.main_page_url)
        return self

    @allure.step("Нажатие по кнопке 'Заказать' вверху страницы")
    def click_first_button(self, browser):
        browser.find_element(*OrderLocators.order_button_header).click()
        return self

    @allure.step("Нажатие по кнопке 'Заказать' внизу страницы")
    def click_second_button(self, browser):
        element = browser.find_element(*OrderLocators.order_button_centre)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return self

    @allure.step("Заполнение поля 'Имя'")
    def user_name(self, browser, name):
        browser.find_element(*OrderLocators.name).send_keys(name)
        return self

    @allure.step("Заполнение поля 'Фамилия'")
    def user_last_name(self, browser, last_name):
        browser.find_element(*OrderLocators.last_name).send_keys(last_name)
        return self

    @allure.step("Заполнение поля 'Адрес'")
    def user_address(self, browser, address):
        browser.find_element(*OrderLocators.address).send_keys(address)
        return self

    @allure.step("Заполнение поля 'Метро'")
    def metro(self, browser, metro):
        browser.find_element(*OrderLocators.metro).send_keys(metro)
        browser.find_element(*OrderLocators.list_station).click()
        return self

    @allure.step("Заполнение поля 'Телефон'")
    def user_phone(self, browser, number):
        browser.find_element(*OrderLocators.number).send_keys(number)
        return self

    @allure.step("Нажатие по кнопке 'Далее' в форме информации о пользователе")
    def click_button_next(self, browser):
        browser.find_element(*OrderLocators.next_button).click()
        return self

    @allure.step("Заполнение поля 'Дата доставки'")
    def date_of_delivery(self, browser, delivery_date):
        browser.find_element(*OrderLocators.delivery_date).send_keys(delivery_date, Keys.ENTER)
        return self

    @allure.step("Заполнение поля 'Срок аренды'")
    def rental_time(self, browser, renta_date):
        browser.find_element(*OrderLocators.renta_date).click()
        select_renta_time_locator = (OrderLocators.select_renta_date[0], OrderLocators.select_renta_date[1].format(renta_date))
        browser.find_element(*select_renta_time_locator).click()
        return self

    @allure.step("Выбор цвета из 2 вариантов")
    def checkbox_color(self, browser, colour):
        if colour == 'чёрный жемчуг':
            browser.find_element(*OrderLocators.colour_black).click()
        elif colour == 'серая безысходность':
            browser.find_element(*OrderLocators.colour_grey).click()
        return self

    @allure.step("Заполнение поля 'Комментарии' к заказу")
    def comment_for_courier(self, browser, comments):
        browser.find_element(*OrderLocators.comments).send_keys(comments)
        return self

    @allure.step("Нажатие по кнопке 'Заказать'")
    def click_button_order(self, browser):
        browser.find_element(*OrderLocators.order_button).click()
        return self

    @allure.step("Нажатие по кнопке 'Да' в окне подтверждения заказа")
    def click_button_yes_in_order(self, browser):
        browser.find_element(*OrderLocators.yes_button).click()
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, browser):
        text_order_created = browser.find_element(*OrderLocators.order_created).text
        assert 'Заказ оформлен' in text_order_created
        return self

    @allure.step("Полный позитивный сценарий - все шаги ввода данных")
    def user_rent_order(self, browser, name, last_name, address, metro, 
                        number, delivery_date, rent_days, colour, comments):
        self.user_name(browser, name)
        self.user_last_name(browser, last_name)
        self.user_address(browser, address)
        self.metro(browser, metro)
        self.user_phone(browser, number)
        self.click_button_next(browser)
        self.date_of_delivery(browser, delivery_date)
        self.rental_time(browser, rent_days)
        self.checkbox_color(browser, colour)
        self.comment_for_courier(browser, comments)
        self.click_button_order(browser)
        self.click_button_yes_in_order(browser)
        self.confirmation_window(browser)
        return self