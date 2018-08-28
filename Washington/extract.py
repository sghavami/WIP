"""

Website:        '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[1]/div/p'
Email:          '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[2]/div/p'
contact:        '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[3]/div/p'
address:        '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[4]/div/p'
hsstart:        '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[5]/div/p'
ehstart:        '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[6]/div/p'
eceap:          '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[7]/div'
lname:          '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[1]/div/p'
lnum:           '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[2]/div/p'
pid:            '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[3]/div/p'
ftype:           '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[4]/div/p'
ages:           '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[5]/div/p'
ldate:          '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[6]/div/p'
Status:         '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[7]/div/p'
ltype:          '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[8]/div/p'
capacity:       '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[9]/div/p'

Provider Contacts:
    //*[@id="ProviderContactsTable"]/tbody/tr[1]/td[1]
    //*[@id="ProviderContactsTable"]/tbody/tr[1]/td[2]
    //*[@id="ProviderContactsTable"]/tbody/tr[1]/td[3]
    //*[@id="ProviderContactsTable"]/tbody/tr[1]/td[4]
    //*[@id="ProviderContactsTable"]/tbody/tr[1]/td[5]

    //*[@id="ProviderContactsTable"]/tbody/tr[2]/td[1]
    //*[@id="ProviderContactsTable"]/tbody/tr[2]/td[2]
    //*[@id="ProviderContactsTable"]/tbody/tr[2]/td[3]
    //*[@id="ProviderContactsTable"]/tbody/tr[2]/td[4]
    //*[@id="ProviderContactsTable"]/tbody/tr[2]/td[5]

Hours of Op:
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[1]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[2]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[3]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[4]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[5]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[6]/div'
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[7]/div'


"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

paths = [
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[1]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[2]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[3]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[4]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[5]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[6]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[1]/div[7]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[1]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[2]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[3]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[4]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[5]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[6]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[7]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[8]/div/p',
    '/html/body/div[2]/div[3]/div[5]/div/div[2]/div[9]/div/p',
    '//*[@id="ProviderContactsTable"]/tbody/tr[1]/td[1]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[1]/td[2]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[1]/td[3]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[1]/td[4]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[1]/td[5]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[2]/td[1]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[2]/td[2]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[2]/td[3]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[2]/td[4]',
    '//*[@id="ProviderContactsTable"]/tbody/tr[2]/td[5]',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[1]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[2]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[3]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[4]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[5]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[6]/div',
    '/html/body/div[2]/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[7]/div'
]

tot = 0
timeout = 4

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)

for line in open('deduped.csv','r').readlines():
    try:
        tot += 1
        if tot <= 5163: continue

        st = line.strip().split(",")
        url = "https://www.findchildcarewa.org/PSS_Provider?id=" + st[0]

        browser.get(url)
        time.sleep(timeout)
        
        for path in paths:
            try:
                sys.stdout.write(browser.find_element_by_xpath(path).text.replace("\r", "").replace("\t", " ").replace("\n", " ") + ",")
            except:
                sys.stdout.write(",")
        sys.stdout.write(line)

        sys.stderr.write("Success: " + `tot` + "\n")
    except Exception, e:
        sys.stderr.write("Error: " + `tot` + " ->" + `e` + "\n")

browser.quit()
