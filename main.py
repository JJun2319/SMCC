from selenium import webdriver
from time import sleep
import os
import sys
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\chromedriver.exe")
driver.get('https://www.scholars.kr/log_in.php')
def login():
    driver.find_element_by_name('userid').send_keys('조영준')
    driver.find_element_by_name('pwd').send_keys("Jun1796!")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="blog"]/div/div[1]/form/table/tbody/tr[1]/td[3]/div').click()


target_url = 'https://www.scholars.kr/pc/dictation_play_data.php?bookno=137&bpage=1'
def su():
    response = requests.get(target_url)
    jsonObj = response.json()
    print(jsonObj.get("etxt"))
