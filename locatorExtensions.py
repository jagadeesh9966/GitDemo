from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.get("https://test.salesforce.com")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,".password").send_keys("shetty")
driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()
driver.find_element(By.XPATH,"//input[@name='cancel']").click()
print(driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR,"form[name='login'] label:nth-child(3)").text)


