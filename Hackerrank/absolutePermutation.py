# https://www.hackerrank.com/challenges/absolute-permutation/problem

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1, 1))
    else:
        num = set(range(1, n + 1))
        result = []
        for i in range(1, n + 1):
            if i <= k:
                if i + k in num:
                    result.append(i + k)
                    num.remove(i + k)
            else:
                if abs(i - k) in num:
                    result.append(abs(i - k))
                    num.remove(abs(i - k))
                elif i + k in num:
                    result.append(abs(i + k))
                    num.remove(abs(i + k))

        return result if len(num) == 0 else [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
