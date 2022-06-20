from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("validateText")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
