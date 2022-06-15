from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_tag_name("Click Here").click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.window_handles[0](driver.window_handles[0])

print(driver.find_element(By.TAG_NAME,"h3").text)

