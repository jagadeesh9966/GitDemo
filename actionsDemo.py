from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(service=Service(executable_path="C:\Softwares\chromedriver"))
'''driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element(By.ID,"mousehover")
action.move_to_element(menu).perform()
childMenu = driver.find_element(By.LINK_TEXT,"Top")
action.move_to_element(childMenu).click().perform()'''
#1st
"""driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element(By.ID,"double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
print(jagadeesh)"""

#2nd program
driver.get("http://www.demo.guru99.com/V4/")
driver.find_element(By.CSS_SELECTOR,"input[name='uid']").send_keys("mngr409462")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("yhUdApA")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
print(driver.title)
print(driver.current_url)
driver.save_screenshot("guru"+str(random.randint(0,70))+".png")
print("jagadeesh")
