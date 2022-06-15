import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
driver.get("http://3.110.88.201/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID,"autosuggest").text)
assert driver.find_element(By.ID,"autosuggest").get_attribute('value') == "India"