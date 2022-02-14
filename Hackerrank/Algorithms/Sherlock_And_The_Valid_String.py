#!/bin/python3

import sys

def isValid(s):
    # Complete this function
    charFreq = {}
    numFreq = {}
    
    for c in s:
        charFreq[c] = charFreq.get(c, 0) + 1
        
    for ck in charFreq.keys():
        numFreq[charFreq[ck]] = numFreq.get(charFreq[ck], 0) + 1
        
    if len(numFreq) <= 1:
        return "YES"
    elif len(numFreq) == 2:
        nk = [f for f in numFreq.keys()]
        if ((nk[0] == 1 or nk[0] - nk[1] == 1) and numFreq[nk[0]] == 1) or ((nk[1] == 1 or nk[1] - nk[0] == 1) and numFreq[nk[1]] == 1): 
            return "YES"
    return "NO"
     
s = input().strip()
result = isValid(s)
print(result)
