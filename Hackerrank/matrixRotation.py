#https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    size = len(matrix[0]) if len(matrix[0]) < len(matrix) else len(matrix)
    nArray = 0
    if size % 2 == 0:
        nArray = int(size / 2)
    else:
        nArray = int((size + 1) / 2)
    # print("Total single array's that will be made - %d"%(nArray))
    tempStorage = []
    tempIndices = []
    topL = 0;
    topR = len(matrix[0]);
    bottomL = len(matrix)
    # print("Size : %s, TopL : %s, TopR : %s, BottomL : %s"%(size,topL,topR,bottomL))
    for i in range(nArray):
        temp = list()
        temp2 = list()
        for x in range(topL, bottomL):
            temp.append(matrix[x][topL])
            temp2.append((x, topL))
        # temp2.append("-")
        for x in range(topL + 1, topR):
            temp.append(matrix[bottomL - 1][x])
            temp2.append((bottomL - 1, x))
        # temp2.append("-")
        if (topR - 1 != topL):
            for x in range(bottomL - 2, topL - 1, -1):
                temp.append(matrix[x][topR - 1])
                temp2.append((x, topR - 1))
        # temp2.append("-")
        if (bottomL - 1 != topL):
            for x in range(topR - 2, topL, -1):
                temp.append(matrix[topL][x])
                temp2.append((topL, x))

        tempStorage.append(temp)
        tempIndices.append(temp2)
        # print(temp)
        # print(temp2)
        topL += 1
        topR -= 1
        bottomL -= 1
    # print(tempStorage)
    # print(tempIndices)

    for i in range(nArray):
        mod = len(tempStorage[i])
        for x in range(mod):
            # print((tempIndices[i][x][0]))
            matrix[int(tempIndices[i][x][0])][int(tempIndices[i][x][1])] = tempStorage[i][int((x - r) % mod)]

    for i in matrix:
        for j in i:
            print("%d" % (j), end=" ")
        print()

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
