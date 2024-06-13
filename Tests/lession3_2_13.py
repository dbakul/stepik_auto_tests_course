from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"
class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control first")]')
        input1.send_keys("Auto")
        input2 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control second")]')
        input2.send_keys("Test")
        input3 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control third")]')
        input3.send_keys("email@test.test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        input4 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control first")]')
        input4.send_keys("Auto")
        input5 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control second")]')
        input5.send_keys("Test")
        input6 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]//input[contains(@class, "form-control third")]')
        input6.send_keys("email@test.test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()