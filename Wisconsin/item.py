#!/usr/local/bin/python

import sys
import time
from geopy import geocoders
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
//*[@id="providerDetailsCollapsible"]/div/div[2]/div[1]
"""

timeout = 3

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)

g = geocoders.GoogleV3(api_key='AIzaSyDLTAVCPoNrLrk5k9zbBa-yNCpJ7KMK57c')

tot = 0
for line in open('urls.txt','r').readlines():
    tot += 1

    browser.get(line.strip())
    time.sleep(timeout)

    try:
        try:
            row = browser.find_element_by_xpath('//*[@id="providerDetailsCollapsible"]/div/div[1]').text.split("\n")[1] + "|"
            path = '//*[@id="providerDetailsCollapsible"]/div/div[3]'
        except:
            row = " |"
            path = '//*[@id="providerDetailsCollapsible"]/div/div[2]'

        st = browser.find_element_by_xpath(path).text.split("\n")
        for i in range(0, len(st)): row += st[i] + "|"

        inputAddress = st[3] + " " + st[4]
        location = g.geocode(inputAddress, timeout=7)
        row += `location.latitude` + "|" + `location.longitude` + "|"

        sys.stdout.write(`len(row.split("|"))` + "|" + row + "\n")
        sys.stderr.write("Success " + `tot` + "\n")
    except Exception, e:
        sys.stderr.write("Error: " + `tot` + " ... " + `e` + "\n")
    #try/except
#for
