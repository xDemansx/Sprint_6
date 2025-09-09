from selenium.webdriver.common.by import By 

import sys 
sys.path.append('..')

# Локаторы - Выпадающий список в разделе «Вопросы о важном».
class FAQLocators:

# локаторы вопросов
    question = [(By.XPATH, '//div[@id="accordion__heading-0"]'),
                (By.XPATH, '//div[@id="accordion__heading-1"]'),
                (By.XPATH, '//div[@id="accordion__heading-2"]'),
                (By.XPATH, '//div[@id="accordion__heading-3"]'),
                (By.XPATH, '//div[@id="accordion__heading-4"]'),
                (By.XPATH, '//div[@id="accordion__heading-5"]'),
                (By.XPATH, '//div[@id="accordion__heading-6"]'),
                (By.XPATH, '//div[@id="accordion__heading-7"]')]
    # локаторы ответов
    answer = [(By.XPATH, '//div[@id="accordion__panel-0"]'),
              (By.XPATH, '//div[@id="accordion__panel-1"]'),
              (By.XPATH, '//div[@id="accordion__panel-2"]'),
              (By.XPATH, '//div[@id="accordion__panel-3"]'),
              (By.XPATH, '//div[@id="accordion__panel-4"]'),
              (By.XPATH, '//div[@id="accordion__panel-5"]'),
              (By.XPATH, '//div[@id="accordion__panel-6"]'),
              (By.XPATH, '//div[@id="accordion__panel-7"]')]