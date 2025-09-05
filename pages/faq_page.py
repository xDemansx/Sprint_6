import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from conftest import browser
from locators.faq_locators import FAQLocators

import sys 
sys.path.append('..')

# Методы работы с вопросами и ответами
class QuestionPage:

    @allure.step("Открываем браузер")
    def open_browser(self, browser):
        browser.get(URLs.main_page_url)
        return self
    
    @allure.step("Ищем список вопросов")
    def scroll_to_faq(self, browser):
        element = browser.find_element(By.CLASS_NAME, "accordion")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        return self
    
    @allure.step("Читаем вопрос")
    def get_question(self, browser, index):
        question_locator = (FAQLocators.question[0], FAQLocators.question[1].format(index))
        question = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(question_locator))
        question.click()
        return question.text
    
    @allure.step("Читаем ответ")
    def get_answer(self, browser, index):
        answer_locator = (FAQLocators.answer[0], FAQLocators.answer[1].format(index))
        answer = browser.find_element(*answer_locator)
        return answer.text