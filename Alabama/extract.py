#XAPATHS
#   search button: '//*[@id="ctl00_ContentPlaceHolder1_LinkButton2"]'
#   first element: '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[2]/span/a'
#   last element: '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[31]/td[2]/span/a'
#
# Paginationjavascript: '__doPostBack('ctl00$ContentPlaceHolder1$GridView1','Page$<page#>')'

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

timeout = 3

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://dhr.alabama.gov/daycare/daycare_search.aspx')


for page in range(1, 85): # 84 pages of 30 items / page
    try:
        if page == 1:   # search for all records and start w/ page 1
            browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_LinkButton2"]').click()
        else:           # go to the next page
            browser.execute_script("__doPostBack('ctl00$ContentPlaceHolder1$GridView1','Page${}')".format(page))
        time.sleep(timeout)

        for i in range (2, 32):         #print item paths
            print browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_GridView1']/tbody/tr[{}]/td[2]/span/a".format(i)).get_attribute("href")

        sys.stderr.write("Success " + `page` + "\n")
    except Exception, e:
        sys.stderr.write("Error " + `page` + ": " + `e` + "\n")
