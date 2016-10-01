#!/usr/bin/python
#encoding=utf-8

import os
import time
import thread
MaxNumbers=100000
counter=[]
def MakeRequest(RequestNo):
    global counter
    tmp=0
    begin = time.time()
    for i in range(MaxNumbers):
        tmp+=1
    end = time.time()
    counter.append(end - begin)

def CreateRequests(ResquestNumbers):
    threadlist = []
    SleepTime = 1
    if ResquestNumbers > 0:
        SleepTime = 1.0 / ResquestNumbers
    for i in range(ResquestNumbers):
        thread = threading.Thread(target=MakeRequest, args=(i, ))
        thread.start()
        threadlist.append(thread)
        time.sleep(SleepTime)
    for thread in threadlist:
        thread.join()
if __name__ == '__main__':
    for i in range(180):
        CreateRequests(100)