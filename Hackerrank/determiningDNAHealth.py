# https://www.hackerrank.com/challenges/determining-dna-health/problem
# !/bin/python3

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
            if len(genes[x]) in healthy:
                if healthy[len(genes[x])][genes[x]] in healthy[len(genes[x])]:
                    healthy[len(genes[x])][genes[x]] = healthy[len(genes[x])][genes[x]] + health[x]
                else:
                    healthy[len(genes[x])].update({genes[x]: health[x]})

            else:
                healthy[len(genes[x])] = {genes[x]: health[x]}
        print(healthy)
        temp = 0;
        # print(d)
        for i in healthy:
            # print(i)
            # print(list(range(0,len(d)-len(i)+1)))
            for x in range(0, len(d) - len(i) + 1):
                # print("%s == %s"%(d[int(x):int(x)+int(len(i))],i))
                if d[int(x):int(x) + int(len(i))] == i:
                    temp += healthy[i]

        # print("Total Health - %s"%(temp))
        if (temp > max):
            max = temp
        if (temp < min):
            min = temp

    print("%d %d" % (min, max))
