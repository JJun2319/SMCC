from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\chromedriver.exe")
def login():
    driver.find_element_by_name('userid').send_keys('YOUR ID')
    driver.find_element_by_name('pwd').send_keys("put ur own pwd")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="blog"]/div/div[1]/form/table/tbody/tr[1]/td[3]/div').click()


