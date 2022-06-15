from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("i am able to automate")
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME,"h3").text)
