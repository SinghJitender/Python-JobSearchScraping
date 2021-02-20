#https://www.hackerrank.com/challenges/countingsort4/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    x = dict()
    for i in range(int(len(arr) / 2)):
        arr[i][1] = "-"
    for i in arr:
        if int(i[0]) in x:
            x[int(i[0])].append(i[1])
        else:
            x[int(i[0])] = [i[1], ]

    for i in sorted(x):
        for j in x[i]:
            print(j, end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)