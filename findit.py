from selenium import webdriver
from time import sleep
import os
import sys
import requests
import json
import re
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\chromedriver.exe")
driver.get('https://www.scholars.kr/log_in.php')
def login():
    driver.find_element_by_name('userid').send_keys('조영준')
    driver.find_element_by_name('pwd').send_keys("Jun1796!")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="blog"]/div/div[1]/form/table/tbody/tr[1]/td[3]/div').click()


def Findbpage():
    html = driver.page_source
    soup = bs(html, 'html.parser')
    state = '미완료'
    status = soup.find_all('div', class_='btn btn-state', text = state)
    print(status)



