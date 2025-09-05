import pytest
from selenium import webdriver

import sys 
sys.path.append('..')

from selenium.webdriver.support.wait import WebDriverWait

# Фикстура инициализации драйвера Firefox
@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window() # Раскрываем на весь экран
    
    yield driver 
    
    driver.quit() # Закрываем браузер ВО ВСЕХ ТЕСТАХ !!!

