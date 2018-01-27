#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    result = []
    scoresSet = sorted(set(scores), reverse=True)     
    index = len(scoresSet)
    for level in alice:     
        rank = 1;
        for i in range(0, index):            
            if level >= scoresSet[i]:                
                index = i               
                break            
            rank += 1         
        result.append(rank)      
    return result
            

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
