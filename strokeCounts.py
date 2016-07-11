#!/usr/bin/python
# encoding: utf-8

from combo import *
from allKanji import *
from kanjiKanas import *
import os

def theSearch(comboPart,kana):
    stringChunk = ''
    for stroke in strokeNumbers:
        if stroke[0] == comboPart:
            for sound in kana:
                if sound in stroke:
                    stringChunk += sound
    return stringChunk

def theBody(theCombo,kanaList):
    if len(theCombo[0]) != len(kanaList):
        print 'The length of the combo and the kana list do not match!'
        return
    listOfaStrings = []
    for eachCombo in theCombo:
        aString = '('
        for iKana in range(len(kanaList)):
            aString += theSearch(str(eachCombo[iKana]),kanaList[iKana])
            aString += ':'
        aString = aString[:-1]
        aString += ')'
        if aString.count(':') == 0:
            if aString.index(')') > 1:
                listOfaStrings.append(aString)
        if aString.count(':') == 1:
            if aString.index(':') > 1 and aString.index(')') - aString.rindex(':') > 1:
                listOfaStrings.append(aString)
        if aString.count(':') == 2:
            if aString.index(':') > 1 and aString.index(')') - aString.rindex(':') > 1 and aString.rindex(':') - aString.index(':') > 1:
                listOfaStrings.append(aString)
    return listOfaStrings




############# Main ######################

os.system('clear')

kanaList = []
kanjiKeys = ''
for each in kks.keys():
    kanjiKeys += each
    kanjiKeys += '/'
    
kanjiCount = int(raw_input('How many kanji? (1/2/3)\n'))
while kanjiCount not in range(1,4):
    print '\n1, 2, or 3 only please.'
    kanjiCount = int(raw_input('How many kanji? (1/2/3)\n'))
os.system('clear')
print 'Choose from these (' + kanjiKeys + 'special)'
print

for each in range(kanjiCount):
    kanji = raw_input('Kanji' + str(each+1) + '\n')
    if kanji == 'special':
        specialKanji = raw_input('What specific Kanji would you like to use?\n')
        kanaList.append([specialKanji])
    else:
        kanaList.append(kks[kanji])
    print
os.system('clear')

goldCombo = goldenCombo(len(kanaList))
silverCombo = goodCombo(len(kanaList))

silver = theBody(silverCombo,kanaList)
gold = theBody(goldCombo,kanaList)





print
for each in silver:
    print each
print
print 'Golden combo'
for each in gold:
    print each
print
