import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

timeout = 15        # wait periods to have: 1) the page load, 2) the csv file downloaded
baseFolder = "/Users/sghavami/Downloads/"       # download folder
defFileName = "ProviderSearch.csv"      # default file name of the csv extract
baseUrl = "http://families.decal.ga.gov/ChildCare/Results?z="       # search url and query string

zips = []       # cache to track processed zips

#instantiate and maximize a Chrome browser window with all extensions disabled to make it lighter
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)
browser.implicitly_wait(timeout)


for line in open('GA.csv','r').readlines():

    # cache zips to avoid dups
    zip = line.strip()
    if zip in zips: continue;
    zips.append(zip)

    # assemble the url and do HTTP GET
    url = baseUrl + zip
    browser.get(url)

    # save time by checking if no match found; else download and rename the csv extract
    try:
        # check whether there are no matches in the zip code
        browser.find_element_by_class_name('alert-danger')
        print zip + ": no match exists"
    except:
        try:
            # wait until the page is loaded and the 'save to csv' button is active
            element_present = expected_conditions.presence_of_element_located((By.ID, 'Content_Main_btnExportToExcel'))
            WebDriverWait(browser, timeout).until(element_present)
            # click the button
            browser.find_element_by_id('Content_Main_btnExportToExcel').click()

            #give it some time for the download to finish; then rename to the respective zip code
            time.sleep(timeout)
            os.rename(baseFolder + defFileName, baseFolder + zip + '.csv')

            print zip + ": match exists"
        except Exception, e:
            print "ERROR: " + str(e)

# end for

browser.quit()  # close the browser
