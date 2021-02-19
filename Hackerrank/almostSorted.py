# https://www.hackerrank.com/challenges/almost-sorted/problem
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.
def almostSorted(arr):
    arr.insert(0,-1)
    arr.append(1000001)
    result = 0
    count = 0
    vali = -1
    valj = -1
    indexi = -1
    indexj = -1
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i+1]:
            indexi = i+1; vali = arr[i+1]
        if arr[i]>arr[i+1]:
            indexj = i; valj = arr[i]
            if (arr[i]<arr[i+2]) and arr[i+1]>arr[i-1]:
                result = 1; count += 1
                indexj = i+1; valj = arr[i+1]
            elif (arr[i]):

    if count == 0:
        print("yes")
    elif count == 1:
        if result == 1:
            print("yes")
            print("swap %d %d" % (i, i + 1))
        if result == 2:
            print("yes")
            print("reverse %d %d"%(indexi,indexj))
    else:
        print("no")




    print(tempNums)
    print(tempIndexes)



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
