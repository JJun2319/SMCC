from selenium import webdriver
from time import sleep
import os
import sys
import requests
from bs4 import BeautifulSoup as bs
import login
import findit
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\91\\chromedriver.exe")
driver.get('https://www.scholars.kr/log_in.php')



target_url = 'https://www.scholars.kr/pc/dictation_play_data.php?bookno=%d&bpage=1' % findit.findbook()



def su():
    response = requests.get(target_url)
    jsonObj = response.json()
    print(jsonObj.get("etxt"))
