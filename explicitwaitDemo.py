import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
list = []
list2 = []

driver = webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4

for button in buttons:
    list.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

veggies = driver.find_elements(By.CSS_SELECTOR,"p.product-name")
for veg in veggies:
    list2.append(veg.text)

print(list2)
assert list == list2
originalAmout = driver.find_element(By.CSS_SELECTOR,".discountAmt").text

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
discountAmout = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
assert float(discountAmout) < int(originalAmout)

print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
amounts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount

