import secrets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(options=options)
driver.get('https://supplier.meesho.com/')
driver.maximize_window()

time.sleep(5)

loginbutton = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')


loginbutton.click()

emailid = driver.find_element(
    By.XPATH, '//*[@id="mui-1"]')
emailid.send_keys('ronnyronny1992@gmail.com')

password = driver.find_element(
    By.XPATH, '')
password.send_keys('Yash@12345')

submit = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/form/button[2]')
submit.click()
