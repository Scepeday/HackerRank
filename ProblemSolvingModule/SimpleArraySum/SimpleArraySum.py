#!/bin/python3

import math
import os
import random
import re
import sys



def simpleArraySum(ar):
    # Write your code here
    n = 0
    i = 0
    while i < ar_count:
        n = n + ar[i]
        i += 1
    return n 
   
        
    print (n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '/n')
    fptr.close()
