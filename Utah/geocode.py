import sys
import time
from geopy import geocoders

g = geocoders.GoogleV3(api_key='AIzaSyDLTAVCPoNrLrk5k9zbBa-yNCpJ7KMK57c')
for line in open('UT.txt','r').readlines():
    try:
        st = line.strip().replace("\r", " ").split("|")

        location = g.geocode(st[7], timeout=7)
        print `location.latitude` + "|" + `location.longitude` + "|" + line
        sys.stderr.write(st[7] + ": " + `location.latitude` + "..." + `location.longitude`)
    except Exception, e:
        sys.stderr.write("Error: " + line)
