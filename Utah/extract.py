"""

https://ccl.utah.gov/ccl/#/facilities/65704

from urllib2 import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("./All.html"), "html.parser")
spans = soup.find_all("span", {"id" : lambda L: L and L.endswith('_lblDVN')})
for span in spans: print span.text

Legend: //*[@id="main-content-wrapper"]/div/fieldset[1]/legend
License Type:           '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[1]',
Status:                 '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[2]',
Date:                   '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[3]',
street:                 '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/span[1]/text()',
city: //*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/text()[1]
phone: //*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/text()[2]
capacity: //*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/div/text()

"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

paths = [
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/legend',
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[1]',
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[2]',
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[3]',
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]'
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/span[2]'
    '//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/div'
]

timeout = 3

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)

i = 0
for line in open('keys.txt','r').readlines():
    i += 1

    try:
        url = 'https://ccl.utah.gov/ccl/#/facilities/' + line.strip()
        browser.get(url)
        time.sleep(timeout)

        s  = `i` + "|" + line.strip() + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/legend').text + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[1]').text.replace("LICENSE TYPE: ", "") + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[2]').text.replace("STATUS: ", "") + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[2]/div[3]').text.replace("INITIAL REGULATION DATE: ", "") + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/div').text + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]/span[1]').text + "|"
        s += browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset[1]/div/div[1]').text.replace("\n", "|") + "|"

        sys.stdout.write(s + "\n")

        sys.stderr.write("Success " + `i` + "\n")
    except Exception, e:
        sys.stderr.write("Error: " + `i` + ":" + `e` + " <=> " + line)
#for
browser.quit()
