import clipboard
import time
from selenium.webdriver.common.by import By
from Fields import AnalogWatches_Fields as Fields
from selenium.webdriver.common import keys




def AnalogWatches_InventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------
    print("Action : AnalogWatches Inventory Details")
    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('220')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('215')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.HSNCode).click()
    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '9102' == r.text:
            r.click()
            break



    # GST
    driver.implicitly_wait(1)
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
    clipboard.copy(x+" Men's Combo of Black Color Sunglasses with Wallet And Watch And Cable Protector {S2+w2+G4+CP}")
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(keys.Keys.CONTROL + 'v')

    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//ul[@role='menu']/div[2]/div//*[name()='svg']").click()
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.find_element(By.XPATH, Fields.dial_diameter_size).click()
    time.sleep(1)
    dial_diameter_sizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in dial_diameter_sizeList:
        if '20' == r.text:
            r.click()
            break







def AnalogWatches_ProductDetails(driver):

    print("Action : Analog Watches Product Details")

    # Color
    driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'Black' in r.text:
            r.click()
            break

    # DisplayType
    driver.find_element(By.XPATH, Fields.DisplayType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    DisplayTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in DisplayTypeList:
        if 'Analog' == r.text:
            r.click()
            break

    # IdealFor
    driver.find_element(By.XPATH, Fields.IdealFor).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    IdealForList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in IdealForList:
        if 'Men' in r.text:
            r.click()
            break



    # Occasion
    driver.find_element(By.XPATH, Fields.Occasion).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    OccasionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in OccasionList:
        if 'Casual' == r.text:
            r.click()
            break

    # StrapColour
    driver.find_element(By.XPATH, Fields.StrapColour).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    StrapColourList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in StrapColourList:
        if 'Black' in r.text:
            r.click()
            break

    # StrapMaterial
    driver.find_element(By.XPATH, Fields.StrapMaterial).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    StrapMaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in StrapMaterialList:
        if 'Stainless Steel' in r.text:
            r.click()
            break

    # StrapType
    driver.find_element(By.XPATH, Fields.StrapType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    StrapTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in StrapTypeList:
        if 'Chain' in r.text:
            r.click()
            break

    # WaterResistance
    driver.find_element(By.XPATH, Fields.WaterResistance).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WaterResistanceList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WaterResistanceList:
        if 'Yes' in r.text:
            r.click()
            break



    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0, 200)", "")


    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('asdf')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASDFG')

    driver.execute_script("window.scrollBy(0, 500)", "")



def AnalogWatches_OtherAttributes(driver):

    print("Action : AnalogWatches Other Attributes")


    # driver.implicitly_wait(1)
    # # AddOn
    # driver.find_element(By.XPATH, Fields.AddOn).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # AddOnList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in AddOnList:
    #     if 'Belt' in r.text:
    #         r.click()
    #         break

    # # Case
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.Case).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # CaseList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in CaseList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break
    #
    # # CaseBezelMaterial
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.CaseBezelMaterial).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # CaseBezelMaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in CaseBezelMaterialList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break

    # # ClaspType
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.ClaspType).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # ClaspTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in ClaspTypeList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break
    #
    # # DateDisplay
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.DateDisplay).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # DateDisplayList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in DateDisplayList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break

    # # DialColour
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.DialColour).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # DialColourList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in DialColourList:
    #     if 'Black' in r.text:
    #         r.click()
    #         break

    # # DialDesign
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.DialDesign).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # DialDesignList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in DialDesignList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break

    # DialShape
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.DialShape).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    DialShapeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in DialShapeList:
        if 'Round' in r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0, 200)", "")

    # # DualTime
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.DualTime).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # DualTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in DualTimeList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break
    #
    # # Gps
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.Gps).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # GpsList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in GpsList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break
    #
    # # Light
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH, Fields.Light).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # LightList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in LightList:
    #     if 'Solid' in r.text:
    #         r.click()
    #         break

    # Mechanism
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Mechanism).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    MechanismList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MechanismList:
        if 'Quartz' in r.text:
            r.click()
            break


    # NetQuantity
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '3' in r.text:
            r.click()
            break

    # PowerSource
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.PowerSource).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PowerSourceList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PowerSourceList:
        if 'Battery Powered' in r.text:
            r.click()
            break

    # ScratchResistant
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.ScratchResistant).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ScratchResistantList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ScratchResistantList:
        if 'Yes' in r.text:
            r.click()
            break

    # ShockResistance
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.ShockResistance).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ShockResistanceList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ShockResistanceList:
        if 'Yes' in r.text:
            r.click()
            break

    # Description
    driver.implicitly_wait(1)
    clipboard.copy("Men's Combo of Black Color Sunglasses with Wallet And Watch And Cable Protector {S2+w2+G4+CP}")
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')