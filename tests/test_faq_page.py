import allure
import pytest

import sys 
sys.path.append('..')

from data import QuestionsAndAnswers
from conftest import browser
from pages.faq_page import QuestionPage


class TestFaqPages:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном". ОР - все вопросы и ответы должны соответствовать заданным в class QuestionsAndAnswers')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.Questions_And_Answers_List)
    def test_click_questions_and_answers_true(self, browser, index, question, answer):
        question_page = QuestionPage()

        question_page.open_browser(browser) # Открываем браузер
        question_page.scroll_to_faq(browser) # Ищем список вопросов
        question_text = question_page.get_question(browser, index) # Читаем вопрос
        answer_text = question_page.get_answer(browser, index) # Читаем ответ
        
        assert question_text == question # Сравниваем каждый вопрос
        assert answer_text == answer # Сравниваем каждый ответ
        # Все тесты проходят PASSED 