# ！usr/bin/python
# import os

def shift():
    global Card
    global n
    tmp = []
    for i in range(n):
        tmp.append(Card[i])
        tmp.append(Card[n + i])
    Card = tmp[:]
    for i in range(2*n-1):
        print ("%d " %Card[i])
    print("%d" %Card[2*n-1])



if __name__ == '__main__':

    global Card
    Card = []
    global n
    global k
    T = int(input())
    for time in range(T):
        n, k = map(int, input().split())
        Card = list(map(int, input().split()))
        for i in range(k):
            shift()

