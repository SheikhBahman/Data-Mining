# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:35:01 2019

@author: Bahman
"""
import sys
#f = open('zoo.data', 'r')
#x = f.readlines()

x = sys.stdin.readlines()

#x = ["animal_name,hair,feathers,eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,venomous,fins,legs,tail,domestic,catsize,class_type","aardvark,1,0,0,1,0,0,1,1,1,1,0,0,4,0,0,1,1","bass,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,-1","worm,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,7","piranha,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,4","gnat,0,0,1,0,1,0,0,0,0,1,0,0,6,0,0,0,6","oryx,1,0,0,1,0,0,0,1,1,1,0,0,4,1,0,1,1","moth,1,0,1,0,1,0,0,0,0,1,0,0,6,0,0,0,6","skimmer,0,1,1,0,1,1,1,0,1,1,0,0,2,1,0,0,2","crab,0,0,1,0,0,1,1,0,0,0,0,0,4,0,0,0,7","vampire,1,0,0,1,1,0,0,1,1,1,0,0,2,1,0,0,1","slowworm,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,0,3","bass,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,-1"]

legList = [0,2,4,5,6,8]
del x[0]
dataAll = []
for line in x:
    lineS = line.replace('\n','').strip().split(',')  
    newFeatures = []
    for i in range(1, len(lineS)):
        newFeatures.append(int(lineS[i]))
    dataAll.append(newFeatures)
    
data = []
test = []
for item in dataAll:
    legs = [0] * 6
    legs[legList.index(item[-5])] = 1
    nitem = item[:12] + legs + item[13:] 
    if item[-1] == -1:
        test.append(nitem)
    else:
        data.append(nitem)

numberFeatures = len(data[0]) - 1
ClassTypes = {}
ClassTypeIndexe = {}
for i in range(len(data)):
    if data[i][-1] in ClassTypes:
        ClassTypes[data[i][-1]] += 1
        ClassTypeIndexe[data[i][-1]].append(i)
    else:
        ClassTypes[data[i][-1]] = 1
        ClassTypeIndexe[data[i][-1]] = [i]

for item in ClassTypes:
    ClassTypes[item] = (ClassTypes[item] + 0.1) / (len(data) + 0.1 * len(ClassTypes))
    
    
featureClassProb = {}

for item in ClassTypeIndexe:
    newProbFeature = [0] * numberFeatures   
    for index in ClassTypeIndexe[item]:
        newProbFeature = [a + b for a, b in zip(newProbFeature, data[index])]
    sumAll = sum(newProbFeature)
        
    featureClassProb[item] = [(x+0.1)/(sumAll + 0.1 * numberFeatures) for x in newProbFeature]
    
  
for item in test:
    maxclassName = 100
    maxProp = 0.0
    for classN in featureClassProb:
        prop = 1.0
        for i in range(len(item) - 1):
            if item[i] != 0:
                prop *= featureClassProb[classN][i]
             #prop = sum([a*b for a,b in zip(item, featureClassProb[classN])])
        prop *= ClassTypes[classN]
        if prop > maxProp:
            maxProp = prop
            maxclassName = classN
    print(maxclassName)
    #if maxclassName != item[-1]:
       # print(str(maxclassName) + " " + str(item[-1]))
