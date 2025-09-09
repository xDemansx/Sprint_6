import allure
import pytest

import sys 
sys.path.append('..')

from pages.base_page import *
from pages.faq_page import *
from data import QuestionsAndAnswers
from conftest import driver
from pages.faq_page import QuestionPage


class TestFaqPages:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном". ОР - все вопросы и ответы должны соответствовать заданным в class QuestionsAndAnswers')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_answers_true(self, driver, index):
        question_page = QuestionPage(driver) # Открываем браузер
        question_page.scroll_to_faq(index) # Ищем список вопросов
        question_page.click_faq_list(index) # Открываем
        assert question_page.get_question(index) # Сравниваем каждый вопрос
        assert question_page.get_answer(index) # Сравниваем каждый ответ
        # Все тесты проходят PASSED 
