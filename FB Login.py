from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#s=Service("C:\Softwares\chromedriver")

#driver=webdriver.Chrome(service=s)

driver = webdriver.Chrome(executable_path="C:\Softwares\chromedriver")
driver.get("https://www.facebook.com/")

driver.find_element(By.CSS_SELECTOR,"[name='email']").send_keys("9640802036")
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("Jaga1234")
driver.find_element(By.CSS_SELECTOR,"[name='login']").click()
driver.close()