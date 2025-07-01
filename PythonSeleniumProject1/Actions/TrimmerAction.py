import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import TrimmerFields as Fields
from selenium.webdriver.common import keys




def TrimmerInventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------
    print("Action : Trimmer Inventory Details")
    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('550')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('545')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()

    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '8510' == r.text:
            r.click()
            break

    # time.sleep(1)
    driver.implicitly_wait(1)

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()

    driver.implicitly_wait(1)
    GSTList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in GSTList:
        if '18' == r.text:
            r.click()
            break


    # Net Weight
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg2)


    # Product Name
    clipboard.copy('6130 '+x+' Hair Dryer for Men and Women Hair Dryer  (1800 W, Black) & 2025 Cordless Trimmer + Cable Protector')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(keys.Keys.CONTROL + 'v')



    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.find_element(By.XPATH, Fields.LengthSize).click()
    time.sleep(1)
    LengthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in LengthSizeList:
        if '10' == r.text:
            r.click()
            break

    driver.find_element(By.XPATH, Fields.WidthSize).click()
    time.sleep(1)
    WidthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WidthSizeList:
        if '1' == r.text:
            r.click()
            break





def TrimmerProductDetails(driver):

    print("Action : Trimmer Product Details")

    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break


    # BatteryRunTime
    driver.find_element(By.XPATH, Fields.BatteryRunTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BatteryRunTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in BatteryRunTimeList:
        if '55 Mins' in r.text:
            r.click()
            break




    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASDFGHJ')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASDFG')



def TrimmerOtherAttributes(driver):

    print("Action : Trimmer Other Attributes")

    driver.execute_script("window.scrollBy(0,500)", "")
    # AdjustableTrimmingRange
    driver.find_element(By.XPATH, Fields.AdjustableTrimmingRange).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    AdjustableTrimmingRangeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in AdjustableTrimmingRangeList:
        if '10 mm' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # ChargingTime
    driver.find_element(By.XPATH, Fields.ChargingTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ChargingTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ChargingTimeList:
        if '8 Hours' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # ClipSize
    driver.find_element(By.XPATH, Fields.ClipSize).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ClipSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ClipSizeList:
        if '1 mm' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # Color
    driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'Black' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # Frequency
    driver.find_element(By.XPATH, Fields.Frequency).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    FrequencyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in FrequencyList:
        if '100 Hz' in r.text:
            r.click()
            break

    # # Material
    # driver.find_element(By.XPATH, Fields.Material).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in MaterialList:
    #     if 'ABS Plastic' in r.text:
    #         r.click()
    #         break


    # # CordLength
    # driver.find_element(By.XPATH, Fields.CordLength).click()
    # time.sleep(1)
    # driver.implicitly_wait(5)
    # CordLengthList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in CordLengthList:
    #     if '1 Mtr' in r.text:
    #         r.click()
    #         break

    driver.implicitly_wait(1)
    # IdealFor
    driver.find_element(By.XPATH, Fields.IdealFor).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    IdealForList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in IdealForList:
        if 'Unisex' in r.text:
            r.click()
            break
    driver.implicitly_wait(1)

    # NetQuantity
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '2' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # PowerConsumption
    driver.find_element(By.XPATH, Fields.PowerConsumption).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PowerConsumptionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PowerConsumptionList:
        if '100 Watts' in r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,500)", "")

    driver.implicitly_wait(1)
    # Type
    driver.find_element(By.XPATH, Fields.Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'Cordless' in r.text:
            r.click()
            break
    time.sleep(1)

    driver.implicitly_wait(1)
    # Warranty
    driver.find_element(By.XPATH, Fields.Warranty).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyList:
        if '1 Year' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # OperatingVoltage
    driver.find_element(By.XPATH, Fields.OperatingVoltage).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    OperatingVoltageList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in OperatingVoltageList:
        if '100 Volts' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # Rechargeable
    driver.find_element(By.XPATH, Fields.Rechargeable).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    RechargeableList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in RechargeableList:
        if 'Yes' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # UseableWhileCharging
    driver.find_element(By.XPATH, Fields.UseableWhileCharging).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    UseableWhileChargingList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in UseableWhileChargingList:
        if 'Yes' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # WarrantyType
    driver.find_element(By.XPATH, Fields.WarrantyType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyTypeList:
        if 'Repair' in r.text:
            r.click()
            break


    # Description
    clipboard.copy(r'6130 Hair Dryer for Men and Women Hair Dryer  (1800 W, Black) & 2025 Cordless Trimmer + Cable Protector')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')