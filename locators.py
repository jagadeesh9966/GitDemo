from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("rahul")
driver.find_element(By.NAME,"email").send_keys("shetty")
driver.find_element(By.ID,"exampleCheck1").click()

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME,"alert-success").text)

driver.close()

