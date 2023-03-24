from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from seleniumrequests import Firefox

serv_obj = Service("C:/BrowserDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()
driver.get("https://staging.salesta.jp/admin/login")
driver.maximize_window()
driver.find_element(By.ID, 'login-form_tenantId').clear()
driver.find_element(By.ID, 'login-form_tenantId').send_keys('AriSaf')
driver.find_element(By.ID, 'login-form_userId').send_keys('root')
driver.find_element(By.ID, 'login-form_password').send_keys('root')
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[7]/div/div/div/button').click()


act_title = driver.title
exp_title = "Salesta"

if act_title == exp_title:
    print("Login Successful!!")
else:
    print("Login Failed-_-")

driver.close()
