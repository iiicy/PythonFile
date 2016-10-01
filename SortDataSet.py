#!/usr/bin/python
import sys
import os
infile = '/20130429-netflowa-origin-selectout/netflow-origin.txt'
outfile='Day2013-04-01Data.csv'
#infile = 'c:/python-test/1.txt'
#outfile = 'c:/python-test/2.txt'
input = open(infile)
output = open(outfile,'w+')
while (1):
    record = input.readline()
    if not record:
        break
    item = record.split()[2]   #截取2013-04-01这一天的所有记录
    if item=='2013-04-01':
        output.write(record)
output.close()
sorted_lines = sorted(open(outfile), key=lambda l: l.split()[3])
output.close()
open(outfile, 'w').write("".join(sorted_lines))




