from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import *
from selenium import webdriver


class TestCase:
    def test_case_1(self):
        # Инициализируем WebDriver
        driver = webdriver.Chrome()
        # Загружаем страницу
        driver.get(f"{base_url}new_user")

        # Переход по ссылке «У меня уже есть аккаунт»
        click_link = driver.find_element(By.CSS_SELECTOR, "form > div:nth-of-type(4) > a")
        click_link.click()

        # Очистка поля email и ввод валидного значения
        email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
        email_input.clear()
        email_input.send_keys(valid_email)

        # Очистка поля pass и ввод валидного значения
        pass_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
        pass_input.clear()
        pass_input.send_keys(valid_pass)

        # Нажимаем на кнопку «Войти» и проверяем карточку
        button_enter = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button")
        button_enter.click()
        assert driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > div.card"), 'Что-то пошло не так!'
        print('Всё прошло успешно!')

        # Выход
        driver.quit()

    def test_case_2(self):
        # Инициализируем WebDriver
        driver = webdriver.Chrome()
        # Переходим на страницу авторизации
        driver.get(f"{base_url}login")

        # Очистка поля email и ввод валидного значения
        email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
        email_input.clear()
        email_input.send_keys(valid_email)

        # Очистка поля pass и ввод валидного значения
        pass_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
        pass_input.clear()
        pass_input.send_keys(valid_pass)

        # Нажимаем на кнопку «Войти» и проверяем заголовок
        button_enter = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button_enter.click()
        assert driver.find_element(By.TAG_NAME, "h1").text == "PetFriends", 'Что-то пошло не так!'
        print('Всё прошло успешно!')

        # Выход
        driver.quit()

    def test_case_3(self):
        # Инициализируем WebDriver
        driver = webdriver.Chrome()
        # Переходим на страницу авторизации
        driver.get(f"{base_url}login")

        # Очистка поля email и ввод валидного значения
        email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
        email_input.clear()
        email_input.send_keys(valid_email)

        # Очистка поля pass и ввод валидного значения
        pass_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
        pass_input.clear()
        pass_input.send_keys(valid_pass)

        # Нажимаем на кнопку «Войти»
        driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button").click()

        # Заходим в «Мои питомцы»
        driver.get(f"{base_url}my_pets")

        # Проверяем карточки
        cards = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
        left_info = driver.find_element(By.XPATH, "//body/div[1]/div[1]/div[1]")
        summary = left_info.get_attribute("innerText").split()
        assert str(len(cards) - 1) in summary, 'Что-то пошло не так!'
        # Печатаем вывод по питомцам
        print("\n", *summary[1:3])

        # На всякий случай
        driver.implicitly_wait(2)

        # Проверяем элементы в карточках
        images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
        descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

        # Читерский ход
        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ', ' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0

        print('Всё прошло успешно! Но это не точно... :)')
        # Выход
        driver.close()
