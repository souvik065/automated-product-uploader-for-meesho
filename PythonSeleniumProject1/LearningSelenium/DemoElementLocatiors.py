import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://supplier.meesho.com/")

        loginbtn = driver.find_element(By.ID, 'loginbutton')
        loginbtn.click()

        time.sleep(2)

        driver.find_element(By.ID, 'mui-1').send_keys('test@test.com')
        time.sleep(4)


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
