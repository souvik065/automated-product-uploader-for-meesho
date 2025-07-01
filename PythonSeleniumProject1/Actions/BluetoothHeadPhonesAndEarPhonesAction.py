import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import BluetoothHeadPhonesAndEarPhonesFields as Fields
from selenium.webdriver.common import keys





def BluetoothHeadPhonesInventoryDetails(driver,x):
    print('Action : BluetoothHeadPhone Inventory Details')
    # ---------------------- Price, Size and Inventory ---------------------------------

    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('450')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('445')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()

    driver.implicitly_wait(2)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '85183000' == r.text:
            r.click()
            break

    # time.sleep(1)
    driver.implicitly_wait(1)


    # Net Weight
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg2)


    # Product Name
    clipboard.copy('T37 '+x+' TRUE WIRELESS EARBUDS AIRPODS V5.1 WITH 1500 MAH POWER BANK Bluetooth Headset  (Black, True Wireless) + Cable Protector Pack Of 4')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(keys.Keys.CONTROL + 'v')

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()

    driver.implicitly_wait(2)
    GSTList = driver.find_elements(By.XPATH, Fields.GSTList)
    for r in  GSTList:
        if '18' == r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,200)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)
    driver.implicitly_wait(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//input[@id="length_size"]').click()
    time.sleep(1)
    LengthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in LengthSizeList:
        if '10' == r.text:
            r.click()
            break



def BluetoothHeadPhoneProductDetails(driver):
    print('Action : BluetoothHeadPhone Product Details')

    driver.execute_script("window.scrollBy(0,500)", "")


    # BatteryChargeTime
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.BatteryChargeTime).click()

    driver.implicitly_wait(2)
    BatteryChargeTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in BatteryChargeTimeList:
        if '3 Hours' == r.text:
            r.click()
            break

    # Color
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Color).click()

    driver.implicitly_wait(2)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'Black' == r.text:
            r.click()
            break

    # Compatibility
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Compatibility).click()

    driver.implicitly_wait(2)
    CompatibilityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CompatibilityList:
        if 'All Smartphones' in r.text:
            driver.implicitly_wait(5)
            r.click()
            break

    # ModelName
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, Fields.ModelName).send_keys('2in1')

    # PlayTime
    driver.find_element(By.XPATH, Fields.PlayTime).click()

    driver.implicitly_wait(2)
    PlayTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PlayTimeList:
        if '10 Hours' == r.text:
            r.click()
            break

    # Type
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Type).click()

    driver.implicitly_wait(2)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'In The Ear' in r.text:
            driver.implicitly_wait(2)
            r.click()
            break


    # WarrantyPeriod
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WarrantyPeriod).click()

    driver.implicitly_wait(2)
    WarrantyPeriodList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyPeriodList:
        if '1 Year' == r.text:
            r.click()
            break

    # WarrentyType
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WarrentyType).click()

    driver.implicitly_wait(2)
    WarrentyTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrentyTypeList:
        if 'Carry In' in r.text:
            r.click()
            break


    # WaterResistance
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WaterResistance).click()

    driver.implicitly_wait(2)
    WaterResistanceList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WaterResistanceList:
        if 'Yes' == r.text:
            r.click()
            break


    # Country
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Country).click()

    driver.implicitly_wait(2)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break

    # Manufacture Details
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')


def BluetoothHeadPhoneOtherAttributes(driver):
    print('Action : BluetoothHeadPhone Other Details')

    driver.execute_script("window.scrollBy(0,500)", "")

    # Bluetooth Range
    driver.find_element(By.XPATH, Fields.BluetoothRange).click()

    driver.implicitly_wait(1)
    BluetoothRangeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in BluetoothRangeList:
        if '10m' in r.text:
            r.click()
            break

    # BluetoothVersion
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.BluetoothVersion).click()

    driver.implicitly_wait(1)
    BluetoothVersionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in BluetoothVersionList:
        if '5.1' in r.text:
            r.click()
            break

    # ChargingType
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.ChargingType).click()

    driver.implicitly_wait(2)
    ChargingTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ChargingTypeList:
        if 'Micro USB' in r.text:
            r.click()
            break

    # Frequency
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Frequency).click()

    driver.implicitly_wait(2)
    FrequencyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in FrequencyList:
        if '10 Hz' in r.text:
            r.click()
            break

    # # Material
    # driver.implicitly_wait(2)
    # driver.find_element(By.XPATH, Fields.Material).click()
    #
    # driver.implicitly_wait(2)
    # MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in MaterialList:
    #     if 'ABS Plastic' in r.text:
    #         r.click()
    #         break

    # Mic
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Mic).click()

    driver.implicitly_wait(2)
    MicList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MicList:
        if 'Yes' in r.text:
            r.click()
            break

    # NetQuantity
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.NetQuantity).click()

    driver.implicitly_wait(2)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '2' in r.text:
            r.click()
            break

    # NoiceCancelation
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.NoiceCancelation).click()

    driver.implicitly_wait(2)
    NoiceCancelationList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NoiceCancelationList:
        if 'Yes' in r.text:
            r.click()
            break

    # Description
    clipboard.copy(r'Bluetooth 5.0, more stable and faster connection. 2. Fast seconds, Bluetooth 5.0, automatic seconds, with headphones can be used 3. Light, comfortable to wear, free to adjust, not easy to fall off 4. 3.5-4 hours working time per charge for the earbuds, 5-6 times full charge by the charging case. 5. Comfort fit & wide compatibility. Different sized ear tips and in-canel cable-free design provide comfortable fit. Support Bluetooth-enabled devices with version 4.0 and above. 6. Exercise ready: Sweat-resistant with a secure fit thats made to move with you. Specification: Packing list 2*Bluetooth Earphone 1*USB Charging Cable 1*Charging Case 1*User Manual')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')