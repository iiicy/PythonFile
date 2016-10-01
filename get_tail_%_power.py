#!/usr/bin/python
#encoding=utf-8
import os

def svr_tail_power(path):
    uti=[]
    input = open(path)
    while 1:
        record = input.readline()
        if not record:
            break
        uti.append(record.split()[4]) #cpu使用率，格式如 35，40

    if len(uti):
        uti.sort()
        return 150 + 1.5 * uti[-int(0.95*len(uti))]
    else:
        return -1

input1= r'/home/chenyang/Sorted_Svr_Postion_Without_0.csv'
input2= r'/home/chenyang/tuotuo2/chenyang/All_25328_SvrData/'
out_path= '/home/chenyang/servers_tail_95%_power.csv'
result=""
input=open(input1)

SvrTail95Power={} #记录各台服务器95%处功率
SortedSvrTail95Power={} #记录排序后各台服务器95%处功率
while 1:
     record = input.readline()
     if not record:
         break
     #line_no += 1
     info = record.split()
     Tail95Power = svr_tail_power(input2 + info[0])
     if(Tail95Power != -1):
         SvrTail95Power[info[0]] = Tail95Power

SortedSvrTail95Power=sorted(SvrTail95Power.iteritems(),key=lambda asd:asd[1],reverse=True)

for key in SortedSvrTail95Power:
    output.write("%s %f \n"%(key,SortedSvrTail95Power[key]))

