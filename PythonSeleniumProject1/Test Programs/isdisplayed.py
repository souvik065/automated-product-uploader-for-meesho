from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(options=options)

driver.get('https://supplier.meesho.com/')
driver.maximize_window()


loginbutton = '//*[@id="loginbuon"]'


try:
    driver.find_element(By.XPATH, loginbutton).is_displayed()
    print(True)
except (NoSuchElementException) as e:
    print(False)

print("Done")