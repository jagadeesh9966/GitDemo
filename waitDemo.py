import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

