#!/usr/bin/python
#encoding=utf-8
import os
import collections
#----------------------------
def SvrInWhichfile(svrid):
    global MapList
    for filename in MapList:
        if svrid in MapList[filename]:
            return filename

#----------------------------
if __name__=="__main__":
    in_path= r'/home/chenyang/Sorted_Svr_Postion_Without_0.csv'
    out_path= '/home/chenyang/'
    map_path=r'/home/chenyang/svr_setn.csv'
    global MapList=collections.defaultdict(list) #记录服务器id到文件编号的映射，比如(2:90001), (5:90135)
    MapIn=open(map_path)
    while 1:
        MapInfo=MapIn.readline()
        if not record:
         break
        inf=MapInfo.split()
        MapList[inf[1]].append(inf[0])

#----------------------------
    FileName=[] #记录文件名称
    for key in MapList:
        FileName.append(key)
    FileName.sort()  #排序后的文件名称

#----------------------------
    file={} #打开所有待写的文件,
    for i in range(len(FileName)):
        file[FileName[i]]=open(out_path+"file"+FileName[i],'a')

#----------------------------
    input=open(in_path)
    while 1:
        record=input.readline()
        if not record:
            break
        SvrId=record.split()[1]
        fname=SvrInWhichfile(SvrId)
        file[fname].write(record)




