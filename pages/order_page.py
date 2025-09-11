import allure

import sys 
sys.path.append('..')

from pages.base_page import *
from data import *
from locators.order_locators import OrderLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Шаги заказа
class OrderPage(BasePageScooter): 

    @allure.step("Ищем кнопку 'Заказать'")
    def scroll_to_bottom_order(self, number_order):
        if number_order == OrderData.First_Order:
            self.scroll_to_element(OrderLocators.order_button_header)
        else:
            self.scroll_to_element(OrderLocators.order_button_centre)
            self.wait_for_page_load(OrderLocators.order_button_centre)
    
    @allure.step("Нажатие на кнопку 'Заказать'")
    def click_to_bottom_order(self, number_order):
        if number_order == OrderData.First_Order:
            self.click_on_element(OrderLocators.order_button_header)
        else:
            self.click_on_element(OrderLocators.order_button_centre)
        
    @allure.step("Заполнение поля 'Имя'")
    def filling_user_name(self, number_order):
        self.set_element(OrderLocators.name, number_order['name'])

    @allure.step("Заполнение поля 'Фамилия'")
    def filling_last_name(self, number_order):    
        self.set_element(OrderLocators.last_name, number_order['last_name'])

    @allure.step("Заполнение поля 'Адрес'")
    def filling_address(self, number_order):    
        self.set_element(OrderLocators.address, number_order['address'])

    @allure.step("Заполнение поля 'Метро'")
    def filling_metro(self, number_order):
        self.set_element(OrderLocators.metro, number_order['metro'])
        self.click_on_element(OrderLocators.list_station)

    @allure.step("Заполнение поля 'Телефон'")
    def filling_user_phone(self, number_order):
        self.set_element(OrderLocators.number, number_order['number'])

    @allure.step("Нажатие по кнопке 'Далее' в форме информации о пользователе")
    def click_button_next(self):
        self.click_on_element(OrderLocators.next_button)

    @allure.step("Заполнение поля 'Дата доставки самоката' в форме Про аренду")
    def filling_date_of_delivery(self, number_order):
        self.set_element(OrderLocators.delivery_date, number_order['delivery_date'])
        self.click_on_element(OrderLocators.delivery_date)

    @allure.step("Заполнение поля 'Срок аренды'")
    def filling_rental_time(self, number_order):
        if number_order == OrderData.First_Order:
            self.click_on_element(OrderLocators.renta_date)
            self.wait_for_page_load(OrderLocators.renta_long[0])
            self.click_on_element(OrderLocators.renta_long[0])
        else:
            self.click_on_element(OrderLocators.renta_date)
            self.wait_for_page_load(OrderLocators.renta_long[1])
            self.click_on_element(OrderLocators.renta_long[1])

    @allure.step("Выбор цвета из вариантов")
    def checkbox_colour(self, number_order):
        if number_order == OrderData.First_Order:
            self.click_on_element(OrderLocators.colour_black)
        else:
            self.click_on_element(OrderLocators.colour_grey)

    @allure.step("Заполнение поля 'Комментарии' к заказу")
    def filling_comment_for_courier(self, number_order):
        self.set_element(OrderLocators.comments, number_order['comments'])

    @allure.step("Нажатие по кнопке 'Заказать' в окне 'Аренда Самоката'")
    def click_button_order(self):
        self.click_on_element(OrderLocators.order_button)

    @allure.step("Нажатие по кнопке 'Да' в форме подтверждения заказа")
    def click_button_yes_in_order(self):
        self.click_on_element(OrderLocators.yes_button)

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        return 'Заказ оформлен' in self.get_text_from_element(OrderLocators.order_created)
