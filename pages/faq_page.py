import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import *
from data import *
from locators.faq_locators import FAQLocators

import sys 
sys.path.append('..')

# Методы работы с вопросами и ответами
class QuestionPage(BasePageScooter):

    @allure.step("Ищем вопрос [index]")
    def scroll_to_faq(self, index):
        self.scroll_to_element(FAQLocators.question[index])

    @allure.step("Жмем на стрелочку вопроса [index]")
    def click_faq_list(self, index):
        self.click_on_element(FAQLocators.question[index])

    @allure.step("Проверяем вопрос [index]")
    def get_question(self, index):
        self.wait_for_page_load(FAQLocators.question[index])
        return self.get_text_from_element(FAQLocators.question[index]) == QuestionsAndAnswers.Questions_List[index]
    
    @allure.step("Проверяем ответ на вопрос [index]")
    def get_answer(self, index):
        self.wait_for_page_load(FAQLocators.question[index])
        return self.get_text_from_element(FAQLocators.answer[index]) == QuestionsAndAnswers.Answers_List[index]
        