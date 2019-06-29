from selenium import webdriver
import math
import time


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

# Считать элемент со страницы
x_element = browser.find_element_by_css_selector("div.form-group span:nth-child(2)")
x = x_element.text
y = calc(x)
print(y)

# Отправляем в форму
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

# Кликнуть по чекбоксу "Подтверждаю, что являюсь роботом"
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

# Выбрать радиобаттон "Роботы рулят"
option2 = browser.find_element_by_id("robotsRule")
option2.click()

# Отправляем заполненную форму
button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()
