from selenium import webdriver
import re
import lxml
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("C:\\Users\\조영준\\Desktop\\a\\91\\chromedriver.exe")
pattern = re.compile('[(-)]')
def findbook():
    html = driver.page_source
    soup = bs(html, 'lxml')
    state = '미완료'
    data = soup.find('div', class_='btn btn-state', text = state)
    bookno = int(re.findall('\((.+)\)', data['onclick'])[0].split(',')[4].replace("'", ''))
    return bookno
