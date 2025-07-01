from selenium.webdriver.common.by import By

BluetoothHeadPhonesAndEarPhones = "BluetoothHeadPhonesAndEarPhones"
HairDryer = "HairDryer"
Trimmer = "Trimmer"
HairStylers = "HairStylers"
HairStraightener = "HairStraightener"
Wallets = "Wallets"
AnalogWatches = "AnalogWatches"
Sunglasses = "Sunglasses"

def Category_Bluetooth_HeadPhones_And_EarPhones(driver):

    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div/div[1]/div/p[7]').click()  # Consumer electronics
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[2]/div/div[2]/p[9]').click()  # Audio & Video
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[3]/div/div[2]/p[2]').click()  # Headphones & Earphones
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[4]/div/div[2]/p[1]').click()  # Bluetooth Headphones & Earphones


def Category_HairDryer(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Hair Dryer"]').click() # Hair Dryer


def Category_Trimmer(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Trimmers"]').click() # Trimmer


def Category_HairStylers(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Hair Stylers"]').click() # Hair Stylers


def Category_HairStraightener(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Hair Straightener"]').click() # Hair Straightener


def Category_Wallets(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Men Fashion"]').click()  # Men Fashion
    driver.find_element(By.XPATH, '//p[normalize-space()="Accessories"]').click()  # Accessories
    driver.find_element(By.XPATH, '//p[normalize-space()="Wallets"]').click() # Wallets
    driver.find_element(By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body1 css-41h2vb"][normalize-space()="Wallets"]').click() # Wallets


def Category_AnalogWatches(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Men Fashion"]').click()  # Men Fashion
    driver.find_element(By.XPATH, '//p[normalize-space()="Accessories"]').click()  # Accessories
    driver.find_element(By.XPATH, '//p[normalize-space()="Watches"]').click() # Wallets
    driver.find_element(By.XPATH, '//p[normalize-space()="Analog Watches"]').click() # Wallets


def Category_Sunglass(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Men Fashion"]').click()  # Men Fashion
    driver.find_element(By.XPATH, '//p[normalize-space()="Accessories"]').click()  # Accessories
    driver.find_element(By.XPATH, "//div[@class='css-ebwp1h']/div[3]//p[normalize-space()='Sunglasses']").click() # Sunglasses
    driver.find_element(By.XPATH, "//div[@class='css-ebwp1h']/div[4]//p[normalize-space()='Sunglasses']").click() # Sunglasses


def Category(driver, category):
    if category == BluetoothHeadPhonesAndEarPhones:
        Category_Bluetooth_HeadPhones_And_EarPhones(driver)
    elif category == HairDryer:
        Category_HairDryer(driver)
    elif category == Trimmer:
        Category_Trimmer(driver)
    elif category == HairStylers:
        Category_HairStylers(driver)
    elif category == HairStraightener:
        Category_HairStraightener(driver)
    elif category == Wallets:
        Category_Wallets(driver)
    elif category == AnalogWatches:
        Category_AnalogWatches(driver)
    elif category == Sunglasses:
        Category_Sunglass(driver)
