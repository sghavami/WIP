import sys

for line in open('WA.csv','r').readlines():
    st = line.strip().split(",")
    if not len(st) == 37: sys.stdout.write(line)
