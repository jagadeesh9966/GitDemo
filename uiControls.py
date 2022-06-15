from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

c = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(c))
