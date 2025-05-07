#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    x = 0
    y = 0
    r = 0
    for i in range(n):
         x = x + arr [i][i]
         i += 1
    arr.reverse()
    for j in range(n):
        y = y + arr [j][j]
        j += 1
    r = (x - y)
    if r < 0:
        r = r * -1
        return (r)
    else:
         return (r)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

