
"""
s = open("./VAcleansed.html").read()
s = s.replace("\r", " ")
s = s.replace("\t", " ")
s = s.replace("\n", "**")

soup = BeautifulSoup(s, "html.parser")
recs = soup.find_all("tr")

for rec in recs:
    try:
        url = "https://www.dss.virginia.gov" + rec.a['href']
        pid = url.split(";")[1].split("=")[1]
        print pid.replace(";", "")
    except Exception, e:
        sys.stderr.write("Error: " + `e` + "\n")
#for
"""
