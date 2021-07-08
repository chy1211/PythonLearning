from selenium import webdriver
import time

# Setting
Account = "C109193244"
Password = "Henrychy12"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://aais5.nkust.edu.tw/selcrs_std")
element_account = driver.find_element_by_id("UserAccount")
element_account.send_keys(Account)
element_password = driver.find_element_by_id("Password")
element_password.send_keys(Password)
btn_login = driver.find_element_by_id("Login")
btn_login.click()

time.sleep(30)
