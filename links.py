import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import pandas as pd
import re
import csv
import random


options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


df = pd.DataFrame(data)
clear_data = df.loc[1:, 0:4]


def getExternalLinks(bs):
    externalLinks = []
    all_links = []
    all_links_for_frame = []

    for link in bs.find_all('a',href=re.compile('^https:\\/\\/[a-z]{2,3}\\.linkedin\\.com\\/.*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                a = link.attrs['href']
                p = re.compile('((http(s?)://)*([www])*\.|[linkedin])[linkedin/~\-]+\.[a-zA-Z0-9/~\-_,&=\?\.;]+[^\.,\s<]')
                if p.match(a):
                    externalLinks.append(a)
                    all_links.append(externalLinks[0])
    return all_links[0]


for i in range(903,1000):
    work_place = clear_data.loc[i][0]
    city = clear_data.loc[i][1]
    first_name = clear_data.loc[i][2]
    middle_name = clear_data.loc[i][3]
    last_name = clear_data.loc[i][4]
    i+=1
    elems = []
    
    #elem = f'site:linkedin.com/in/ AND {city} AND {first_name} {middle_name} {last_name}'
    elem = f'linkedin.com/in {first_name} {last_name} {work_place}'
    
    elems.append(elem)
    try:
        for e in elems:
            k = 1
            t = random.randint(1,5)
            browser = webdriver.Chrome('chromedriver.exe')
            time.sleep(4)
            browser.get('https://duckduckgo.com/')
            t = random.randint(1,5)
            time.sleep(t)
            search_query = browser.find_element_by_name('q')
            t = random.randint(1,5)
            time.sleep(t)
            search_query.clear()
            t = random.randint(1,5)
            time.sleep(t)
            search_query.send_keys(e)
            t = random.randint(1,5)
            time.sleep(t)
            search_query.send_keys(Keys.RETURN)
            t = random.randint(1,5)
            time.sleep(t)
            bs = BeautifulSoup(browser.page_source, 'lxml')
            try:
                print(getExternalLinks(bs))
                browser.close()
                time.sleep(15)
            except IndexError:
                print('None')
                browser.close()
                time.sleep(15)
    except InvalidElementStateException:
        browser.close()
        browser = webdriver.Chrome('chromedriver.exe')


