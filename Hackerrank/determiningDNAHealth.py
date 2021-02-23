#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())
    min = 999999999
    max = -1
    for s_itr in range(s):

        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        healthy = dict()
        for x in range(first, last + 1):
            key = genes[x]
            lenKey = len(key)
            if lenKey in healthy:
                if key in healthy[lenKey]:
                    healthy[lenKey][key] = healthy[lenKey][key] + health[x]
                else:
                    healthy[lenKey].update({key: health[x]})
            else:
                healthy[lenKey] = {genes[x]: health[x]}
        print(healthy)
        #print(healthy)
        temp = 0;
        #print(d)
        for i in healthy:
            #print(i)
            #print(list(range(0,len(d)-len(i)+1)))
            for x in range(0,len(d)-i+1):
                #print("%s == %s"%(d[int(x):int(x)+int(len(i))],i))
                spl = d[x:x+i]
                if spl in healthy[i]:
                    temp += healthy[i][spl]

        #print("Total Health - %s"%(temp))
        if( temp>max):
            max = temp
        if(temp<min):
            min = temp

    print("%d %d"%(min,max))
