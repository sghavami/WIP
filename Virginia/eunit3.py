import sys
import string
from geopy import geocoders
from urllib2 import urlopen
from bs4 import BeautifulSoup

goog = geocoders.GoogleV3(api_key='AIzaSyDLTAVCPoNrLrk5k9zbBa-yNCpJ7KMK57c')
for line in open('ids.txt','r').readlines():
    pid = line.strip()
    try:

        url = "https://www.dss.virginia.gov/facility/search/cc2.cgi?rm=Details;ID=" + pid
        content = urlopen(url).read().replace("\r", " ").replace("\t", " ").replace("\n", "**")

        soup = BeautifulSoup(content, "html.parser")
        cell = soup.find_all('td')

        st = cell[0].text.strip().split("**")
        i = 1 if len(st[0].strip()) < 3 else 0
        name = st[i].strip()
        address = st[i+1].strip() + ", " + cell[1].text.replace("**", "").strip()

        phone = cell[2].text.replace("**", "").strip()
        type = cell[4].text.replace("**", "").strip()
        license = cell[6].text.replace("**", "").strip()
        expiration = cell[8].text.strip().replace("**", "").strip()
        admin = name
        hours = cell[10].text.replace("**", "").strip()
        capacity = "Not Available"
        ages = "Not Available"
        inspector = cell[12].text.replace("**", "").strip()
        subsidy = cell[14].text.replace("**", "").strip()

        location = goog.geocode(address, timeout=10)
        loc = `location.latitude` + "|" + `location.longitude`

        print pid + "|" + name + "|" + address + "|" + type + "|" + capacity + "|" + loc + "|" + phone + "|"  + license + "|" + expiration + "|" + admin + "|" + hours + "|"  + ages + "|" + inspector + "|" + subsidy
        content = ""

    except Exception, e:
        sys.stderr.write("Error: " + pid + "..." + `e` + "\n")
#for
