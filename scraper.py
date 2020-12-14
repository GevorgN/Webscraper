import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login')

#Need to write your email and password in config.txt file
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)


time.sleep(5)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

#Put LinkedIn link here
link = ''

browser.get(link)

last_height = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    # Scroll down to bottom
    time.sleep(5)
    #see_more_button.click()
    time.sleep(5) 
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);") 
    # Wait to load page
    time.sleep(5)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
           break
    last_height = new_height


bs = BeautifulSoup(browser.page_source, 'lxml')

info = []

name_div = bs.find('div', {'class': 'flex-1 mr5'})
name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()

location = name_loc[1].find('li').get_text().strip()
profile_title = name_div.find('h2').get_text().strip()

connection = name_loc[1].find_all('li')
connection = connection[1].get_text().strip()

info.append(link)
info.append(name)
info.append(location)
info.append(profile_title)
info.append(connection)

print(info)
