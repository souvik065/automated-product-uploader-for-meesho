import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# strs = 'document.querySelector("settings-ui").shadowRoot.querySelector("settings-main#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("#clearBrowsingDataConfirm.action-button")'




# driver.get('https://supplier.meesho.com/')
# driver.maximize_window()


def PreparingCache(driver):
    start = time.time()
    print("Action : Preparing Cache")
    parentwindow = driver.current_window_handle

    driver.implicitly_wait(10)
    driver.execute_script('window.open("https://www.google.com", "new window")')
    all_handlers = driver.window_handles

    for handel in all_handlers:
        if handel != parentwindow:
            driver.switch_to.window(handel)
            driver.get('chrome://settings/clearBrowserData')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("settings-ui").shadowRoot.querySelector("settings-main#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("settings-checkbox[id=\'cookiesCheckboxBasic\']").shadowRoot.querySelector("cr-checkbox").shadowRoot.querySelector("div#checkbox").click();')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("settings-ui").shadowRoot.querySelector("settings-main#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("#clearBrowsingDataConfirm.action-button").click();')
            time.sleep(2)

    driver.switch_to.window(parentwindow)
    time.sleep(5)
    end = time.time()
    t = end-start
    print("Time Taken : "+str(t))


def ClearCache(driver):

    start = time.time()
    print("Action : Clearing Cache")
    all_handlers = driver.window_handles

    parentwindow = driver.current_window_handle
    for handel in all_handlers:
        if handel != parentwindow:
            driver.switch_to.window(handel)
            for s in range(1, 4):
                driver.get('chrome://settings/clearBrowserData')
                time.sleep(1)
                driver.execute_script('document.querySelector("settings-ui").shadowRoot.querySelector("settings-main#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("#clearBrowsingDataConfirm.action-button").click();')
                time.sleep(1)

            all_handlers = driver.window_handles
            parentwindow = driver.current_window_handle
            for handel in all_handlers:
                if handel != parentwindow:
                    driver.switch_to.window(handel)
                    time.sleep(1)

    end = time.time()
    t = end - start
    print("Time Taken : "+str(t))

