from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)
try:
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    alert = driver.switch_to.alert
    alert.accept()
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()