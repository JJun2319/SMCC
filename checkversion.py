from selenium import webdriver
import chromedriver_autoinstaller

def checkVersion():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

    driver.implicitly_wait(10)