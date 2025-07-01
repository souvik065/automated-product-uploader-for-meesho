import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import HairStylersFields as Fields
from selenium.webdriver.common import keys





def HairStylersInventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------
    print("Action : Hair Stylers Inventory Details")
    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('220')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('215')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()

    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '8516' == r.text:
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
    clipboard.copy('2009 NV '+x+' 2 IN 1 Hair Curler & Hair Straightener & Cable Protector')
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
        if '1' == r.text:
            r.click()
            break

    driver.find_element(By.XPATH, Fields.WidthSize).click()
    time.sleep(1)
    WidthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WidthSizeList:
        if '10' == r.text:
            r.click()
            break





def HairStylersProductDetails(driver):

    print("Action : Hair Stylers Product Details")

    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break


    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')
    driver.execute_script("window.scrollBy(0,200)", "")


def HairStylersOtherAttributes(driver):

    print("Action : Hair Stylers Other Attributes")


    # driver.implicitly_wait(1)
    # # Color
    # driver.find_element(By.XPATH, Fields.Color).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in ColorList:
    #     if 'Black' in r.text:
    #         r.click()
    #         break


    # CordLength
    driver.find_element(By.XPATH, Fields.CordLength).click()
    time.sleep(1)
    driver.implicitly_wait(5)
    CordLengthList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CordLengthList:
        if '1 Mtr' in r.text:
            r.click()
            break

    # HeatUpTime
    driver.find_element(By.XPATH, Fields.HeatUpTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    HeatUpTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HeatUpTimeList:
        if '10 Sec' in r.text:
            r.click()
            break

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

    driver.implicitly_wait(1)
    # Material
    driver.find_element(By.XPATH, Fields.Material).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MaterialList:
        if 'Plastic' in r.text:
            r.click()
            break

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
    # PowerConsumption
    driver.find_element(By.XPATH, Fields.PowerConsumption).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PowerConsumptionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PowerConsumptionList:
        if '1000 Watts' in r.text:
            r.click()
            break

    driver.implicitly_wait(1)
    # Temperature
    driver.find_element(By.XPATH, Fields.Temperature).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TemperatureList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TemperatureList:
        if '100' in r.text:
            r.click()
            break



    driver.implicitly_wait(1)
    # Type
    driver.find_element(By.XPATH, Fields.Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'Wireless' in r.text:
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
    clipboard.copy('Straight or curl, take your pick with the this 2-in-1 Straightening and Curling hair Iron. You no longer need to have a flat iron for silky straight hair and a curling iron to create bouncy curls. Whether it is for your office every day or a dinner with friends, give your hair that straight, chic look with the help of this hair straightener.Patented Coating. It has a patented coating which makes it easy for you to straighten your hair. The patented floating, ceramic plates ensure high-quality grooming for your hair. It heats up in 30 seconds, so you can get started on your hair styling in no time. Compact. This hair straightener has a sleek and compact body, so it can easily fit into your handbag or travel bag. The 360-degree rotating cord makes it easy for you to style your hair and also ensures easy storage.')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')