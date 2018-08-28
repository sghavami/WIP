from geopy import geocoders
import os
import sys
import string

codes = dict()
counter = 0
cursor = 0

g = geocoders.GoogleV3(api_key='AIzaSyDLTAVCPoNrLrk5k9zbBa-yNCpJ7KMK57c')
with open("all.csv") as f:
    for line in f:
        cursor += 1

        fields = line.strip().split(",")
        if len(fields) < 10: continue
        code = fields[0]

        try:
            if not code in codes:
                inputAddress = fields[3] + ' ' + fields[4] + ' ' + fields[5] + ' ' + fields[6]
                location = g.geocode(inputAddress, timeout=10)
                codes[code] = `location.latitude` + "," + `location.longitude` + ","
                counter += 1

            print codes[code] + line.strip()
        except Exception, e:
            sys.stderr.write(`cursor` + " : " + str(e) + "\n")
    #end for
f.close()
sys.stderr.write(`cursor` + ":" + `counter` + "\n")


"""
inputAddress = '1333 H St. NW, Washington, DC'
location = g.geocode(inputAddress, timeout=10)
print(location.latitude, location.longitude)


files = glob.glob("./GA/*.csv")
for file in files:
    lines = open(file).read().split('\r')
    if len(lines) <= 1: continue

    for i in range(1, len(lines)):
        cursor += 1
        s = re.sub('^\x20-\x7f', '', lines[i])
        stoken = lines[i][2:].split(",")
        print lines[i][2:]
        counter += 1
        #s = filter(lambda x: x in string.printable, lines[i])[1:]
        #if len(s) > 1: print s
    #end for
#end for
#print `cursor` + ":" + `counter`


re.sub(r'[^\x00-\x7f]',r'', your-non-ascii-string)
s = re.sub('\W+', '', lines[i])
def cleanse_data (path)
    files = glob.glob(path)
    for file in files:
        lines = open(file).read().split('\r')
        if len(lines) <= 1: continue

        for i in range(1, len(lines)):
            s = filter(lambda x: x in string.printable, lines[i])[1:]
            if len(s) > 1: print s
        #end for
    #end for
# end def
print `len(files)` + ":" + `counter`
    for line in lines:
        cursor += 1
        sys.stdout.write(line.strip("\r"))
        continue

        fields = line.strip().split(",")
        if len(fields) < 10: continue

        code = fields[0]

        if not code in codes:
            try:
                qstring = fields[3].replace(' ', '+') + '+' + fields[4].replace(' ', '+') + '+' + fields[5].replace(' ', '+') + '+' + fields[6].replace(' ', '+')
                url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + qstring

                #response = requests.get(url)
                #result = response.json()
                #codes[code] = `result['results'][0]['geometry']['location']['lat']` + "," + `result['results'][0]['geometry']['location']['lng']`
                codes[code] = "lat,lng"
                counter += 1
            except:
                pass

        print codes[code] + "," + line.strip()
#end for

print `len(files)` + ":" + `cursor` + ":" + `counter`

"""
