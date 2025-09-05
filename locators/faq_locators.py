from selenium.webdriver.common.by import By 

import sys 
sys.path.append('..')

# Локаторы - Выпадающий список в разделе «Вопросы о важном».
class FAQLocators:
    question = (By.XPATH, "(//div[@class='accordion__button'])[{}]") # Вопрос
    answer = (By.XPATH, "(//div[@class='accordion__panel'])[{}]") # Ответ
