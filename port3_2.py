from selenium import webdriver

import time
import os
import random
import selenium.webdriver.chrome.options
import selenium.webdriver.support.ui as ui
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXTENSION_PATH = './system/extension_10_2_0_0.crx'

def changeWindowHandles(switchTo):
    setRestartCount()
    try:
        # switchTo
        if not driver.window_handles[switchTo]:
            time.sleep(1)
            changeWindowHandles(switchTo)
            return

        driver.switch_to.window(driver.window_handles[switchTo])
        resetRestartCount()
    except:
        time.sleep(1)
        changeWindowHandles(switchTo)

def resetRestartCount():
    global restartCount
    restartCount = 0

def setRestartCount():
    global restartCount
    restartCount += 1
    global driver

    if restartCount > 30:
        restartCount = 0
        global driver
        time.sleep(1)
        print("重啟")
        start(driver)

# 點擊
def clickPath(by, xpath):
    setRestartCount()
    try:
        link = driver.find_element(by, xpath)
        if not link:
            time.sleep(1)
            clickPath(by, xpath)
            return

        link.click()
        resetRestartCount()
    except:
        time.sleep(1)
        clickPath(by, xpath)

def metaMaskNavigate(driver):
    clickPath("//button[@class='button btn-primary first-time-flow__button']")
    clickPath('//button[text()="匯入錢包"]')
    clickPath('//button[text()="No Thanks"]')
    time.sleep(10000)

    global safeCheckButtonValue
    if safeCheckButtonValue.get():
        global msgString
        msgString.set("請自行輸入註記詞與密碼後點選匯入，下一部將會繼續自動執行")
    else:
        inputs = driver.find_elements_by_xpath('//input')
        time.sleep(1)
        clickPath('//button[text()="匯入"]')

    clickPath('//button[text()="都完成了"]')

    return driver

def start(driver):
    index = 0
    while True:
        changeWindowHandles(0)
        index += 1
        if index % 2 == 0:
            new_url = 'https://soquest.xyz/bql/discovery/655346b05365effe2d23881d'
            if driver.current_url != new_url:
                driver.get(new_url)

            time.sleep(1)
            clickPath(By.CSS_SELECTOR, "button#\:R1ljal9lm\:")
            time.sleep(1)
            changeWindowHandles(2)
            clickPath(By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'btn-primary') and contains(@class, 'page-container__footer-button') and contains(text(), '確認')]")
        else:
            new_url = 'https://soquest.xyz/bql/discovery/655347f3900ac5f85e143c6f'
            if driver.current_url != new_url:
                driver.get(new_url)

            time.sleep(1)
            clickPath(By.CSS_SELECTOR, "button#\:R1ljal9lm\:")
            time.sleep(1)
            changeWindowHandles(2)
            clickPath(By.XPATH, "//button[contains(text(), '確認')]")

        time.sleep(40)

global restartCount
restartCount = 0

opt = webdriver.ChromeOptions()
opt.add_argument("--lang=zh_TW")
opt.add_extension(EXTENSION_PATH)

chrome_driver_path = "./system/chromedriver.exe"
global driver
driver = webdriver.Chrome(options=opt)

# 打开Google网站
driver.get("https://www.google.com")
time.sleep(1)

driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

clickPath(By.CLASS_NAME, "button.btn-primary.first-time-flow__button")
time.sleep(1)

clickPath(By.CLASS_NAME, "button.btn-primary.first-time-flow__button")
time.sleep(1)

clickPath(By.CSS_SELECTOR, "button[data-testid='page-container-footer-next']")
time.sleep(1)

input1 = driver.find_element(By.XPATH, "//input[@placeholder='Paste Secret Recovery Phrase from clipboard']")
input1.send_keys("raise bundle expire science nasty raw mechanic connect near globe erode brown")

input2 = driver.find_element(By.ID, "password")
input2.send_keys("ASD123123wqe@@@")

input3 = driver.find_element(By.ID, "confirm-password")
input3.send_keys("ASD123123wqe@@@")
time.sleep(1)

checkbox = driver.find_element(By.CLASS_NAME, "first-time-flow__checkbox.first-time-flow__terms")
checkbox.click()
time.sleep(1)

clickPath(By.XPATH, "//button[@class='button btn-primary first-time-flow__button' and @type='submit']")
time.sleep(1)

clickPath(By.CLASS_NAME, "button.btn-primary.first-time-flow__button")
time.sleep(1)
driver.get('https://soquest.xyz/mining?invite_code=tDrVY7')

time.sleep(30)
# 這裡可以手動輸入自己的私鑰

clickPath(By.XPATH, "//button[contains(text(), 'Connect')]")
time.sleep(1)

clickPath(By.XPATH, "//span[contains(text(), 'MetaMask')]/ancestor::div[@role='button']")

time.sleep(1)

changeWindowHandles(2)

clickPath(By.CLASS_NAME, "button.btn-primary")
time.sleep(1)

clickPath(By.XPATH, "//button[@data-testid='page-container-footer-next']")
time.sleep(5)

clickPath(By.XPATH, "//button[@data-testid='request-signature__sign']")
time.sleep(5)

changeWindowHandles(0)

clickPath(By.XPATH, "//button[contains(@class, 'MuiIconButton-root') and contains(@class, 'MuiIconButton-colorPrimary') and contains(@class, 'MuiIconButton-sizeMedium')]")
time.sleep(1)

clickPath(By.XPATH, "//span[text()='Polygon']")
time.sleep(1)

changeWindowHandles(2)

time.sleep(1)

clickPath(By.XPATH, "//button[text()='Approve']")

time.sleep(1)

clickPath(By.XPATH, "//button[text()='Switch network']")

time.sleep(1)
changeWindowHandles(0)
time.sleep(1)
driver.get('https://soquest.xyz/bql/discovery/655346b05365effe2d23881d')

clickPath(By.XPATH, "//button[contains(text(), 'Accept')]")
time.sleep(1)

clickPath(By.CSS_SELECTOR, "button#\:R1ljal9lm\:")
time.sleep(1)

clickPath(By.CLASS_NAME, "PrivateSwitchBase-input")
time.sleep(1)

clickPath(By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-sizeMedium') and contains(text(), 'Continue')]")
time.sleep(1)

start(driver)

