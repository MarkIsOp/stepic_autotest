from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
)
button.click()
x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
)
x = calc(x_element.text)
field = browser.find_element(By.ID, "answer")
field.send_keys(x)
submit = browser.find_element(By.ID, "solve")
submit.click()

time.sleep(10)