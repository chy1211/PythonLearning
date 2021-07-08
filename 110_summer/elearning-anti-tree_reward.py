from selenium import webdriver
import time

# Setting
Account = "*"
Password = "*"


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://elearning.nkust.edu.tw/mooc/login.php")
times = 0
while times < 1219:

    element_account = driver.find_element_by_id("username")
    element_account.send_keys(Account)
    element_password = driver.find_element_by_id("password")
    element_password.send_keys(Password)
    btn_login = driver.find_element_by_id("btnSignIn")
    btn_login.click()
    driver.get("https://elearning.nkust.edu.tw/logout.php")
    time.sleep(2)
    driver.get("https://elearning.nkust.edu.tw/mooc/login.php")
    times += 1
    print(f"目前執行到第{times}次,還剩下{1219-times}次")
