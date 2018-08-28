import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

timeout = 3

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://ccl.utah.gov/ccl/#/facilities')
time.sleep(timeout)
elem = browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset/ol[2]/li/input').click()

j = 0
for page in range (1, 86):
    try:
        time.sleep(timeout)

        for i in range (1, 26):
            try:
                path = '//*[@id="main-content-wrapper"]/div/fieldset/div[3]/table/tbody/tr[' + `i` + ']/td[1]/a'
                print `j*25+i`, browser.find_element_by_xpath(path).get_attribute("href").replace('https://ccl.utah.gov/ccl/#/facilities/', '')
            except:
                print `j*25+i`, 'bad'
        # for

        elem = browser.find_element_by_xpath('//*[@id="main-content-wrapper"]/div/fieldset/div[3]/div[2]/span/input')
        elem.clear()
        page += 1
        elem.send_keys(`page`)
        elem.send_keys(Keys.RETURN)

        sys.stderr.write("Success " + `page` + "\n")
    except Exception, e:
        sys.stderr.write("Error " + `page` + ": " + `e` + "\n")
    j += 1
#for
