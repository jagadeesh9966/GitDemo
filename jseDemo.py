from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("jaga")
print(driver.find_element(By.NAME,"name").text)
print(driver.find_element(By.NAME,"name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

shopButton = driver.find_element(By.CSS_SELECTOR,"a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
