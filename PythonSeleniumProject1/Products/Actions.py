import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# Email Accounts
shreejulejha_ronny = "ronnyronny1992@gmail.com"
shribalaji = "shribalajimotersagar@gmail.com"
thegiftarea = "thegiftarea.in@gmail.com"
atrsmarketing = "artsmarketing.in@gmail.com"
prohra8 = "PROHRA8@GMAIL.COM"

# email_AC = shreejulejha_ronny
# email_AC = shribalaji
# email_AC = thegiftarea
email_AC = atrsmarketing
# email_AC = prohra8



# @jit(nopython=True)
def Login(driver):
    print("Action : Login")

    loginbutton = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
    loginbutton.click()

    time.sleep(2)

    emailid = driver.find_element(
        By.XPATH, '//*[@id="mui-1"]')
    emailid.send_keys(email_AC)

    password = driver.find_element(
        By.XPATH, '//*[@id="mui-2"]')
    password.send_keys('Yash@12345')

    submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/form/button[2]')
    submit.click()



    # time.sleep(10)
    wait = WebDriverWait(driver, 25, ignored_exceptions=[ElementClickInterceptedException])
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/nav/div/div/div/div[2]/div[2]/div/ul/div/div[6]/li')))
    driver.implicitly_wait(15)

    catlogupload = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/div/div[2]/div[2]/div/ul/div/div[6]/li')
    catlogupload.click()

    # time.sleep(5)
    driver.implicitly_wait(15)







