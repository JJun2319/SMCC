from selenium import webdriver
from time import sleep
import os
import sys
import requests
import json
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\chromedriver.exe")
driver.get('https://www.scholars.kr/log_in.php')
def login():
    driver.find_element_by_name('userid').send_keys('조영준')
    driver.find_element_by_name('pwd').send_keys("Jun1796!")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="blog"]/div/div[1]/form/table/tbody/tr[1]/td[3]/div').click()

maxbp = None
nowbp = ()

target_url = 'https://www.scholars.kr/pc/dictation_play_data.php?bookno=137&bpage={0}'.format(nowbp)

def start():
    global idxmnbp
    idxmnbp = driver.find_element_by_xpath('//*[@id="pop_dictation1"]/div[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div').text
    maxbp = idxmnbp[4:]
    nowbp = idxmnbp[:1].rstrip
    response = requests.get(target_url)
    jsonObjs = response.json()
    answer = jsonObjs{'etxt'}
    print (answer)
    #jsonObj = response.json()
    #print(jsonObj.get("etxt"))




    
    


