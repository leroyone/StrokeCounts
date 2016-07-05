#!/usr/bin/python

def combo():
    excellent = [6,15,24,31,47,63]
    veryGood = [1,3,5,11,13,16,21,23,29,32,33,37,39,41,45,52,65,67,68]
    good = [7,8,17,18,25,35,38,48,57,58,61,71,73,75,77,78]
    bad = [14,22,26,27,28,30,42,43,46,49,50,51,53,55,56,59,72,74,2,4,12,34,36,40,44,54,60,62,64,66,69,70,76,79,80,9,10,19,20]
    
    allLists = excellent + veryGood + good + bad
    goodList = excellent + veryGood + good
    
    combos = []
    
    for each in allLists:
        for i in allLists:
            if each + i == 15 and each + i + 6 in goodList:
                combos.append([each,i])
    
    return combos