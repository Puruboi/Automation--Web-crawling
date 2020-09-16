# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 13:44:49 2020

@author: Puruboi_since_1998
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import Inputhandler


# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='WhatsApp.log', level=logging.INFO)

# setting options for chrome driver
options = Options()

#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")

def info(msg1='',msg2='',msg3=''):
    logging.info(str(msg1)+str(msg2)+str(msg3))
    print(msg1,msg2,msg3)
    
    
info("<WhatsApp>  trying to connecting to url", ' at ',time.ctime())

path = r"C:\Users\Anonymous\Desktop\Puruboi\chromedriver.exe"
driver = webdriver.Chrome(path)
url='https://web.whatsapp.com/'
driver.get(url)
time.sleep(5)


for i in range(1,5,1):
    search_box_xpath = '(//*[@id="side"]/div[1]/div/label/div/div[2])'

    Inputhandler.mouseClickSendKeyandEnter(driver,search_box_xpath,'Puruboi')
    time.sleep(1)
    Type_message_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    Inputhandler.mouseClickSendKeyandEnter(driver,Type_message_xpath,'Hy hello')
    time.sleep(2)


    Inputhandler.mouseClickSendKeyandEnter(driver,search_box_xpath,'Praveen_vade')
    time.sleep(1)
    Inputhandler.mouseClickSendKeyandEnter(driver,Type_message_xpath,'hello')
    time.sleep(2)


time.sleep(2)
driver.close()

