#!/bin/python3

import sys
import math

s = input().strip()

l = len(s)
minVal = math.floor(math.sqrt(l))
maxVal = math.ceil(math.sqrt(l))
rows, cols = 0, 0

if (minVal*minVal >= l):
    rows, cols = minVal, minVal
else:
    rows, cols = maxVal, maxVal
    
newS = ""
for i in range(cols):
    for j in range(i, l, cols):
        newS += s[j]
    newS += " "
    
print(newS)
