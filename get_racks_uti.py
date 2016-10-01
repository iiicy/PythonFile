#!/usr/bin/python
#encoding=utf-8
import os

def svr_average_uti(path):
    uti=[]
    input = open(path)
    while 1:
        record = input.readline()
        if not record:
            break
        uti.append(record.split()[4]) #cpu使用率，格式如 35，40
    if not len(uti):
        return sum(uti)*1.0/len(uti)
    else:
        return 0

input1= r'/home/chenyang/Sorted_Svr_Postion_Without_0.csv'
input2= r'/home/chenyang/tuotuo2/chenyang/All_25328_SvrData/'
out_path= '/home/chenyang/racks_uti.csv'
input=open(input1)
line_no=0
RackAveUti=[] #记录各台机架平均使用率
SvrAveUti=[] #记录各台机架内服务器平均cpu使用率
record = input.readline()
base_rank_no = int(record.split()[1])
#cnt=1 #记录各个机架内服务器数量
while 1:
     record = input.readline()
     if not record:
         break
     #line_no += 1
     info=record.split()
     rank_no = int(info[1])
     if rank_no == base_rank_no:
         #cnt += 1
         AveUti = svr_average_uti(input2+info[0])
         SvrAveUti.append(AveUti)

     else:
         base_rank_no = rank_no
         #cnt = 1
         power=0
         for item in SvrAveUti:
             power = power + (150 + 1.5 * item)
         RackAveUti.append(power/4400)
         SvrAveUti=[]

RackAveUti.sort()
output = open(out_path, 'w')
for item in RackAveUti:
    output.write(item)
    output.write("\n")
