import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

counties = {
'Adams' : 33,
'Asotin' : 12,
'Benton' : 141,
'Chelan' : 110,
'Clallam' : 46,
'Clark' : 239,
'Columbia' : 4,
'Cowlitz' : 45,
'Douglas' : 73,
'Ferry' : 1,
'Franklin' : 147,
'Garfield' : 1,
'Grant' : 148,
'GraysHarbor' : 52,
'Island' : 48,
'Jefferson' : 6,
#'King' : 2008,
'Kitsap' : 150,
'Kittitas' : 22,
'Klickitat' : 9,
'Lewis' : 47,
'Lincoln' : 6,
'Mason' : 34,
'Okanogan' : 37,
'Pacific' : 12,
'PendOreille' : 3,
'Pierce' : 559,
'SanJuan' : 6,
'Skagit' : 98,
'Skamania' : 6,
'Snohomish' : 518,
'Spokane' : 275,
'Stevens' : 15,
'Thurston' : 213,
'Wahkiakum' : 2,
'WallaWalla' : 51,
'Whatcom' : 120,
'Whitman' : 21,
'Yakima' : 348
}

timeout = 5

for county in counties:
    try:
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        browser = webdriver.Chrome(chrome_options=options)
        #browser.implicitly_wait(timeout)
        browser.get("https://www.findchildcarewa.org/PSS_Search?p=DEL%20Licensed;Unlicensed%20Facility&PSL-0030=Open&PSL-0026=" + county)
        time.sleep(timeout)

        #read # of matches
        #i = [int(s) for s in browser.find_element_by_xpath('//*[@id="resultCount"]').text.split() if s.isdigit()][0]

        i = counties[county]
        j = 1
        sys.stderr.write(county + ": %d ... " % i)

        while j <= i:

            try:
                gmap = browser.find_element_by_xpath('//*[@id="resultsList"]/div[%d]/div[2]/div/div[2]' % j)
                gcont = gmap.find_element_by_xpath('.//*[starts-with(@id, "map_")]')
                gurl = gmap.find_element_by_xpath('//*[@id="' + gcont.get_attribute("id") + '"]/div/div/div[7]/div[2]/a')
                st = gurl.get_attribute("href").split('@')[1].split(',')

                elem = browser.find_element_by_xpath('//*[@id="resultsList"]/div[%d]/div[3]/div/div[1]/a' % j)

                browser.execute_script("return arguments[0].scrollIntoView();", elem)
                print elem.get_attribute("href").split("=")[1] + ',' + st[0] + ',' + st[1] + ','

                #sys.stderr.write("\t%d: \n" % j)
                j += 1
            except Exception, e:
                sys.stderr.write("Warning at %d: " % j + `e` + "\n")
                time.sleep(timeout)
        #while
        sys.stderr.write(" processed %d ... \n" % j)

    except Exception, e:
        sys.stderr.write("Error: " + `e` + "\n")

    browser.quit()
#for
