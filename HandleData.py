#!/usr/bin/python
#encoding=utf-8
import os

infile= r'/home/chenyang/Sorted_Svr_Postion.csv'
outfile= '/home/chenyang/Sorted_Svr_Postion_Without_0_1.csv'
input=open(infile)
output=open(outfile,'w')
for i in range(126):
    input.readline()
while 1:
    record = input.readline()
    if not record:
        break
    output.write(record)
input.close()
output.close()
