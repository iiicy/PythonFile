#!/usr/bin/python
#encoding=utf-8
import os

infile= r'/home/chenyang/Sorted_Svr_Postion_Without_0.csv'
input=open(infile)
line_no=0
SvrDsy=[] #记录各台机架内服务器数量
record = input.readline()
base_rank_no = int(record.split()[1])
cnt=1 #记录各个机架内服务器数量
while 1:
     record = input.readline()
     if not record:
         break
     line_no += 1
     rank_no = int(record.split()[1])
     if rank_no == base_rank_no:
         cnt += 1
     else:
         base_rank_no = rank_no
         cnt = 1
         SvrDsy.append(cnt)
print(sum(SvrDsy)*1.0/len(SvrDsy))