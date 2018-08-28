#XAPATHS
#   Name:       //*[@id="ctl00_ContentPlaceHolder1_Label1"]/div[1]/div[2]/span
#   Facility:   //*[@id="ctl00_ContentPlaceHolder1_Label1"]/div[2]/div[2]/span
#   Status:     //*[@id="ctl00_ContentPlaceHolder1_Label1"]/text()[1]
#   Contact:    //*[@id="ctl00_ContentPlaceHolder1_Label1"]/b[2]
#   Phone:      //*[@id="ctl00_ContentPlaceHolder1_Label1"]/text()[2]
#   DayHours:   //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[1]/table/tbody/tr[1]/td[1]
#   NiteHours:  //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[1]/table/tbody/tr[1]/td[2]
#   DayAge:     //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[1]/table/tbody/tr[2]/td[1]
#   NiteAge:    //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[1]/table/tbody/tr[2]/td[2]
#   Street:     //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[3]
#   City:       //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[4]
#   State:      //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[5]
#   Zip:        //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[6]
#   Street:     //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[8]
#   City:       //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[9]
#   State:      //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[10]
#   Zip:        //*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[11]
#

import sys
import time
from geopy import geocoders
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    s = line.strip()
    try:
        browser.get(line.strip())
        id = line.strip().split("=")[1]
        time.sleep(timeout)

        s  = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[8]').text.strip() + " "
        s += browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[9]').text.strip() + " "
        s += browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[10]').text.strip() + " "
        s += browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/span[11]').text.strip()

        location = g.geocode(s, timeout=7)
        s = id + "|" + `location.latitude` + "|" + `location.longitude`

        s += "|" + browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/div[1]/div[2]/span').text.strip()
        s += "|" + browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]/div[2]/div[2]/span').text.strip()
        s += "|" + browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Label1"]').text.replace("\n", "|").strip()

        print "|" + s

        sys.stderr.write("Success " + `tot` + "\n")
    except Exception, e:
        sys.stderr.write("Error " + `tot` + ": " + `e` + "\n")
