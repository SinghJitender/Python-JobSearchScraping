#https://www.hackerrank.com/challenges/countingsort4/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    print(arr)
    x = dict()
    y = set()
    for i in range(len(arr)/2):
        arr[i][1] = "-"
    for i in arr:
        if i[0] in x:
            x[i[0]].append(i[1])
        else:
            x[i[0]] = [i[1]]
            y.add(i[0])
    print(x)
    print(y)
    sorted(y)
    print(y)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)