#!/bin/python3

import sys

def query(w, ls):
    c = 0
    for s in ls:
        if w == s:
            c += 1
    return c

ls = []
n = int(input().strip())
for i in range(n):
    ls.append(str(input().strip()))
q = int(input().strip())
for j in range(q):
    s = str(input().strip())
    print(query(s, ls))
 