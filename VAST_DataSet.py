#!/usr/bin/python
import sys
import os

infile = '/home/chenyang/20130429-netflowa-origin-selectout/netflow-origin.txt'
#infile = 'c:/python-test/2.txt'
fread = open(infile)
count=1
requests=[]
record=fread.readline() #先取出第一个时间，判断以后的是否与其相同
time = record.split()[3]

while (1):
    record = fread.readline()
    if not record:
        requests.append(count)
        break
    item = record.split()[3]
    if item==time:
        count+=1
    else :
        time=item
        requests.append(count)
        count=1
print (requests)
