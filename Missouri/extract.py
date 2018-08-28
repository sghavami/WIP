"""
DVN:                '//*[@id="ctl00_ContentPlaceHolder1_lblDVN"]',
Name:               '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityName"]',
Address:            '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityAddress"]',
City:               '//*[@id="ctl00_ContentPlaceHolder1_lblCity"]',
State:              '//*[@id="ctl00_ContentPlaceHolder1_lblState"]',
Zip:                '//*[@id="ctl00_ContentPlaceHolder1_lblZipCode"]',
County:             '//*[@id="ctl00_ContentPlaceHolder1_lblCounty"]',
Phone:              '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityPhone"]',
Email:              '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityEmail"]',
Type:               '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityType"]',
Date:``             '//*[@id="ctl00_ContentPlaceHolder1_lblLicenseeEffectiveDate"]',
Exipration:         '//*[@id="ctl00_ContentPlaceHolder1_lblLicenseeExpirationDate"]',
Capacity:           '//*[@id="ctl00_ContentPlaceHolder1_lblTotalCapacity"]',
Ages:               '//*[@id="ctl00_ContentPlaceHolder1_lblAgeRange"]',
HoursFrom:          '//*[@id="ctl00_ContentPlaceHolder1_lblHoursFrom"]',
HoursTo:            '//*[@id="ctl00_ContentPlaceHolder1_lblHoursTo"]'

https://webapp01.dhss.mo.gov/childcaresearch/Facility.aspx?LID=002586385

from urllib2 import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("./All.html"), "html.parser")
spans = soup.find_all("span", {"id" : lambda L: L and L.endswith('_lblDVN')})
for span in spans: print span.text
"""
import sys
import time
from geopy import geocoders
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

paths = [
    '//*[@id="ctl00_ContentPlaceHolder1_lblDVN"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityName"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityAddress"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblCity"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblState"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblZipCode"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblCounty"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityPhone"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityEmail"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblFacilityType"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblLicenseeEffectiveDate"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblLicenseeExpirationDate"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblTotalCapacity"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblAgeRange"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblHoursFrom"]',
    '//*[@id="ctl00_ContentPlaceHolder1_lblHoursTo"]'
]

tot = 0
timeout = 3

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)

for line in open('ids.txt','r').readlines():
    try:
        tot += 1
        id = line.strip()
        url = "https://webapp01.dhss.mo.gov/childcaresearch/Facility.aspx?LID=" + id
        browser.get(url)
        time.sleep(timeout)

        sys.stdout.write(`tot` + "|" + id + "|")
        for path in paths:
            try:
                sys.stdout.write(browser.find_element_by_xpath(path).text.replace("\r", "").replace("\t", " ").replace("\n", " ") + "|")
            except:
                sys.stdout.write("N/A|")
        sys.stdout.write("\n")

        sys.stderr.write("Success: " + `tot` + "\n")
    except Exception, e:
        sys.stderr.write("Error: " + `tot` + ":" + `e` + "\n")

browser.quit()

#
