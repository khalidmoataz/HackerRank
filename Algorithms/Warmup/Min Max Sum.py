import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    values=[]
    s = sum(arr)
    for num in arr:
        values.append(s - num)
    print(min(values) , max(values))
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
