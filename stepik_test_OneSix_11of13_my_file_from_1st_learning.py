from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_xpath('//div[contains(@class, "first_block")]//input[contains(@class, "form-control first")]').send_keys('Antoshka')
    browser.find_element_by_xpath('//div[contains(@class, "first_block")]//input[contains(@class, "form-control second")]').send_keys('Kartoshka')
    browser.find_element_by_xpath('//div[contains(@class, "first_block")]//input[contains(@class, "form-control third")]').send_keys('pochta@gmail.com')
    browser.find_element_by_xpath('//div[contains(@class, "second_block")]//input[contains(@class, "form-control first")]').send_keys('88005553535')
    browser.find_element_by_xpath('//div[contains(@class, "second_block")]//input[contains(@class, "form-control second")]').send_keys('Russia, Moscow')
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
