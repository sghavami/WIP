import sys
import time
from geopy import geocoders

g = geocoders.GoogleV3(api_key='AIzaSyDLTAVCPoNrLrk5k9zbBa-yNCpJ7KMK57c')
tot = 0
for line in open('MO.txt','r').readlines():
    tot += 1
    try:
        st = line.strip().split("|")
        inputAddress = st[4] + ", " + st[5] + " " + st[6] + " " + st[7]
        location = g.geocode(inputAddress, timeout=10)
        print line.strip() + `location.latitude` + "|" + `location.longitude`

        sys.stderr.write("Success: " + `tot` + "\n")
    except Exception, e:
        sys.stderr.write("Error: " + `tot` + ":" + `e` + "\n")
