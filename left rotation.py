
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])
import math
    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    shifted = a[d%n:] + a[:d%n]
    for num in shifted:
        print(num, end=' ')
