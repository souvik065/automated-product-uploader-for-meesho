
import  clipboard
import time

from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Fields import HairStraightenerFields as Fields
from selenium.webdriver.common import keys



def HairStraightenerInventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------

    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('480')

    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('475')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.HSNCode)))
    driver.find_element(By.XPATH, Fields.HSNCode).click()
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '8516' == r.text:
            r.click()
            break



    # Net Weight
    Wait = WebDriverWait(driver, 25)
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.Weight)))
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')


    # Product Name
    clipboard.copy('N-1290 '+x+' Hair Dyer + Mini Straightener + 216 trimmer Personal Care Appliance Combo + cable protector (Hair Dryer, Hair Straightener, Trimmer, cable protector )')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(keys.Keys.CONTROL + 'v')

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    GSTList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in  GSTList:
        if '18' == r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.Size)))
    driver.find_element(By.XPATH, Fields.Size).click()


    # wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException])
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]')))
    time.sleep(1)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="presentation"]//button[2]')))
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')


def HairStraightenerProductDetails(driver):

    print('Action : Hair Dryer Product Details')

    # CordLength
    driver.find_element(By.XPATH, Fields.CordLength).click()
    time.sleep(1)
    driver.implicitly_wait(5)
    CordLengthList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CordLengthList:
        if '1 Mtr' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    # NetQuantity
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '3' == r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    # WarrantyPeriod
    driver.find_element(By.XPATH, Fields.WarrantyPeriod).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    WarrantyPeriodList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyPeriodList:
        if '1 Year' == r.text:
            driver.implicitly_wait(5)
            r.click()
            break


    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')
    driver.execute_script("window.scrollBy(0,500)", "")


def HairStraightenerOtherAttributes(driver):

    print('Action : Hair Dryer Other Attributes')

    # # Color
    # driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    # driver.implicitly_wait(5)
    # ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in ColorList:
    #     if 'Multicolor' in r.text:
    #         driver.implicitly_wait(5)
    #         r.click()
    #         break



    # HeatUpTime
    driver.find_element(By.XPATH, Fields.HeatUpTime).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    HeatUpTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HeatUpTimeList:
        if '10 Sec' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    driver.implicitly_wait(5)
    # IdealFor
    driver.find_element(By.XPATH, Fields.IdealFor).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    IdealForList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in IdealForList:
        if 'Unisex' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break
    driver.implicitly_wait(5)


    driver.implicitly_wait(5)
    # Material
    driver.find_element(By.XPATH, Fields.Material).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MaterialList:
        if 'Plastic' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break


    driver.implicitly_wait(5)
    # OperatingVoltage
    driver.find_element(By.XPATH, Fields.OperatingVoltage).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    OperatingVoltageList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in OperatingVoltageList:
        if '100 Volts' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    driver.implicitly_wait(5)
    # PowerConsumption
    driver.find_element(By.XPATH, Fields.PowerConsumption).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    PowerConsumptionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PowerConsumptionList:
        if '1000 Watts' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break


    driver.implicitly_wait(5)
    # StraightningType
    driver.find_element(By.XPATH, Fields.StraightningType).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    StraightningTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in StraightningTypeList:
        if 'Temporary' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break


    driver.implicitly_wait(5)
    # Temperature
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.Temperature)))
    driver.find_element(By.XPATH, Fields.Temperature).click()

    driver.implicitly_wait(5)
    TemperatureList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TemperatureList:
        if '100' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break


    # Type
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.Type)))
    driver.find_element(By.XPATH, Fields.Type).click()

    driver.implicitly_wait(5)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'Wired' in r.text:
            r.click()
            time.sleep(1)
            break




    driver.implicitly_wait(5)
    # WarrantyType
    wait = WebDriverWait(driver, 5, ignored_exceptions=[ElementClickInterceptedException])
    wait.until(EC.element_to_be_clickable((By.XPATH, Fields.WarrantyType)))
    driver.find_element(By.XPATH, Fields.WarrantyType).click()
    driver.implicitly_wait(5)
    WarrantyTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyTypeList:
        if 'Repair' in r.text:
            r.click()
            break

        # WarrantyPeriod
    driver.find_element(By.XPATH, Fields.Warranty).click()
    # time.sleep(1)
    driver.implicitly_wait(5)
    WarrantyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyList:
        if '1 Year' == r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    # Description
    clipboard.copy('N-1290 Hair Dyer + Mini Straightener + 216 trimmer Personal Care Appliance Combo + cable protector (Hair Dryer, Hair Straightener, Trimmer, cable protector )')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')