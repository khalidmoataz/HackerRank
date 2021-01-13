import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    x=0
    y=0
    for i in range(len(arr)):
        x+=arr[i][i]
        y+=arr[i][len(arr)-1-i]
    return abs(x-y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
