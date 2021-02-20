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
    tempNums = []
    tempIndexes = []
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] <arr[i+1] :
            pass
        else:
            tempNums.append(arr[i])
            tempIndexes.append(i)

    descOrder = True
    for i in range(len(tempNums) - 1):
        if not tempNums[i] > tempNums[i + 1]:
            descOrder = False

    if (descOrder):
        if arr[tempIndexes[0] - 1] < tempNums[-1] and arr[tempIndexes[-1] + 1] > tempNums[0] and len(tempNums) > 2:
            print("yes")
            print("reverse %d %d" % (tempIndexes[0], tempIndexes[-1]))
        elif arr[tempIndexes[0] - 1] < tempNums[-1] and arr[tempIndexes[-1] + 1] > tempNums[0] and len(tempNums) == 2:
            print("yes")
            print("swap %d %d" % (tempIndexes[0], tempIndexes[-1]))
        else:
            print("no")
    else:
        if(len(tempNums) == 4):
            temp1 = tempNums[0]
            temp2 = tempNums[-1]
            arr[tempIndexes[0]] = temp2
            arr[tempIndexes[-1]] = temp1
            aescorder = True
            for i in range(len(arr)-1):
                if not arr[i] < arr[i+1]:
                    aescorder = False
                    break;
            if aescorder:
                print("yes")
                print("swap %d %d"%(tempIndexes[0],tempIndexes[-1]))
            else :
                print("no")
        else:
            print("no")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
