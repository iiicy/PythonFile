#!/usr/bin/python
import sys
import os

infile='/home/chenyang/requestsNum.csv'
outfile='/home/chenyang/top1800requestsNum.dat'
input=open(infile)
output=open(outfile,'w')
input.readline()
for i in range(1800):
    item=input.readline()
    output.write(item)