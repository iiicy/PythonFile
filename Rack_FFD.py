#!/usr/bin/python
#encoding=utf-8
import os
import collections
ServerListPath= r'/home/chenyang/servers_tail_95%_power.csv'
AllSvrDataPath= r'/home/chenyang/tuotuo2/chenyang/All_25328_SvrData/'
out_path= '/home/chenyang/advanced_racks_uti.csv'

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
        return -1

SvrsIdPwr={} #记录服务器的id以及95%处功率
MaxRackNum=3000
Racks=[4400]* MaxRackNum
SvrsInWhichRack=collections.defaultdict(list) #记录各台服务器放置在哪个机架上
RackUti=[]
input = open(ServerListPath)
while 1:
    record=input.readline()
    if not record:
        break
    info=record.split()
    SvrsIdPwr[info[0]]=float(info[1])
for key in SvrsIdPwr.keys():
    for index in range(MaxRackNum):
        if Racks[index] >= SvrsIdPwr[key]:
           Racks[index] -= SvrsIdPwr[key]
           SvrsInWhichRack[index].append(key)
           break

UsedRacksNo=0
for index in range(MaxRackNum): #计算使用的机架数
    if Racks[index]<4400:
        UsedRacksNo += 1
    else:
        break


for index in range(UsedRacksNo):
    RackPwr=0
    for SvrID in SvrsInWhichRack[index]:
        AveUti=svr_average_uti(AllSvrDataPath + SvrID)
        if AveUti!=-1:
            RackPwr += 1.5*RackPwr+150
    RackUti.append(RackUti/4400)

RackUti.sort()
output=open(out_path,'w')
for item in RackUti:
    output.write(item+"\n")