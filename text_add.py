from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)
with open('a.txt', 'a+', encoding='utf-8') as f:
    f.close()
try:

    fname = driver.find_element(By.NAME, "firstname").send_keys("Name")
    lname = driver.find_element(By.NAME, "lastname").send_keys("Last name")
    email = driver.find_element(By.NAME, "email").send_keys("email")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "a.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = driver.find_element(By.TAG_NAME, "button")

    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()