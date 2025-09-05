from selenium.webdriver.common.by import By 

import sys 
sys.path.append('..')

# Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката». 
# Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
class LogoLocators:
    yandex_button = (By.XPATH, '//a[@href="//yandex.ru"]') # Логотип "Яндекс"
    scooter_button = (By.XPATH, '//a[@href="/"]') # Логотип "Самокат"
    dzen_logo = (By.XPATH, '//a[@data-testid = "logo"]') # Локатор Логотипа на странице "Дзен"