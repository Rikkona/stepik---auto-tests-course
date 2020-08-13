from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), str(100))
        )

    button = browser.find_element_by_id('book')
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # enter y
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button2 = browser.find_element_by_id('solve')
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()