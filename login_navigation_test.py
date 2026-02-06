from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

print("Login Message:",
      driver.find_element(By.ID, "flash").text)

driver.find_element(By.CSS_SELECTOR,
                    "a.button.secondary.radius").click()
time.sleep(2)

print("Logout Message:",
      driver.find_element(By.ID, "flash").text)

driver.quit()
