import clipboard
import time

from argon2 import Type
from selenium.webdriver.common.by import By
from Fields import Wallet_Fields as Fields
from selenium.webdriver.common import keys




def Wallet_InventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------
    print("Action : Wallet Inventory Details")
    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('135')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('133')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()

    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '4202' == r.text:
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
    clipboard.copy('21'+x+' Gift Hamper for Men | Black Wallet and Brown Belt Men\'s Combo Gift Set | Leather Wallets for Men | Men\'s Wallet {B1+W2}')
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
        if '10' == r.text:
            r.click()
            break





def Wallet_ProductDetails(driver):

    print("Action : Wallet Product Details")

    # Color
    driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'Brown' in r.text:
            r.click()
            break

    # Material
    driver.find_element(By.XPATH, Fields.Material).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MaterialList:
        if 'Canvas & Leather' in r.text:
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



    # NoOfCompartments
    driver.find_element(By.XPATH, Fields.NoOfCompartments).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NoOfCompartmentsList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in NoOfCompartmentsList:
        if '5' in r.text:
            r.click()
            break

    # Type
    driver.find_element(By.XPATH, Fields.Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in TypeList:
        if 'Card & ID Cases' in r.text:
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


    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')

    driver.execute_script("window.scrollBy(0, 500)", "")



def Wallet_OtherAttributes(driver):

    print("Action : Wallet Other Attributes")


    driver.implicitly_wait(1)
    # CardSlot
    driver.find_element(By.XPATH, Fields.CardSlot).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CardSlotList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CardSlotList:
        if '1 - 5 Slots' in r.text:
            r.click()
            break

    # Pattern
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Pattern).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PatternList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PatternList:
        if 'Solid' in r.text:
            r.click()
            break




    # Description
    driver.implicitly_wait(1)
    clipboard.copy(r'21A Gift Hamper for Men | Black Wallet and Brown Belt Men\'s Combo Gift Set | Leather Wallets for Men | Men\'s Wallet {B1+W2}')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')