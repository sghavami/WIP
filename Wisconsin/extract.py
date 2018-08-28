"""
search: https://childcarefinder.wisconsin.gov/Search/SearchResults.aspx?q=90-6F-A9-CE:MHwwfHwgfHx8fDB8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXwtMXwtMXxGYWxzZXw0MHxhfDB8MHx8ZHxGYWxzZXwwfEZhbHNl
item: https://childcarefinder.wisconsin.gov/provider/providerdetails.aspx?ProviderNumber=2000557872&LocationNumber=21&q=90-6F-A9-CE%3aMHwwfHwgfHx8fDB8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXwtMXwtMXxGYWxzZXw0MHxhfDB8MHx8ZHxGYWxzZXwwfEZhbHNl

//*[@id="ctl00_BodyCPH_gvSearchResults"]/tbody/tr[1]/td[3]/a
//*[@id="ctl00_BodyCPH_gvSearchResults"]/tbody/tr[2]/td[3]/a
//*[@id="ctl00_BodyCPH_gvSearchResults"]/tbody/tr[25]/td[3]/a
//*[@id="ctl00_BodyCPH_gvSearchResults_ctl29_pagerControl1_lbNext"]

"""
#!/usr/local/bin/python
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

timeout = 5

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://childcarefinder.wisconsin.gov/Search/SearchResults.aspx?q=90-6F-A9-CE:MHwwfHwgfHx8fDB8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXxUcnVlfFRydWV8VHJ1ZXwtMXwtMXxGYWxzZXw0MHxhfDB8MHx8ZHxGYWxzZXwwfEZhbHNl')

for page in range (1, 194):
    try:
        time.sleep(timeout)

        for i in range (1, 26):
            path = '//*[@id="ctl00_BodyCPH_gvSearchResults"]/tbody/tr[' + `i` + ']/td[3]/a'
            print browser.find_element_by_xpath(path).get_attribute("href")
        # for
        browser.find_element_by_xpath('//*[@id="ctl00_BodyCPH_gvSearchResults_ctl29_pagerControl1_lbNext"]').click()

        sys.stderr.write("Success " + `page` + "\n")
    except Exception, e:
        sys.stderr.write("Error " + `page` + ": " + `e` + "\n")
#for
