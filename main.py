from selenium import webdriver
from time import sleep
import os
import sys
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("PUT PATH FOR Chromedriver.exe")
driver.get('https://www.scholars.kr/log_in.php')




def findbook():
    html = driver.page_source
    soup = bs(html, 'lxml')
    state = '미완료'
    data = soup.find('div', class_='btn btn-state', text = state)
    bookno = int(re.findall('\((.+)\)', data['onclick'])[0].split(',')[4].replace("'", ''))
    return bookno

target_url = 'https://www.scholars.kr/pc/dictation_play_data.php?bookno=%d&bpage=1' % findit.findbook()

def login():
    driver.find_element_by_name('userid').send_keys('PUT UR OWN ID')
    driver.find_element_by_name('pwd').send_keys("PUT UR PWD")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="blog"]/div/div[1]/form/table/tbody/tr[1]/td[3]/div').click()

def su():
    response = requests.get(target_url)
    jsonObj = response.json()
    print(jsonObj.get("etxt"))
