# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:49:47 2019

@author: Bahman
"""

import math

with open('partitions.txt', 'r') as f:
    lines = f.readlines()    
    groundData = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        groundData[idData] =idCluster    #attanetion this one is different format

with open('clustering_1.txt', 'r') as f:
    lines = f.readlines()    
    cluster1 = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        cluster1[idData] =idCluster
        
        
with open('clustering_2.txt', 'r') as f:
    lines = f.readlines()    
    cluster2 = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        cluster2[idData] =idCluster
        
with open('clustering_3.txt', 'r') as f:
    lines = f.readlines()    
    cluster3 = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        cluster3[idData] =idCluster
        
        
with open('clustering_4.txt', 'r') as f:
    lines = f.readlines()    
    cluster4 = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        cluster4[idData] =idCluster
        
        
with open('clustering_5.txt', 'r') as f:
    lines = f.readlines()    
    cluster5 = {}
    for line in lines:
        idData, idCluster = line.strip().split()
        cluster5[idData] =idCluster
        
def createTable(cData, ground):
    table = {}
    for item in cData:
        predictedC = cData[item]
        trueC = ground[item]
        
        if predictedC not in table:
            table[predictedC] = {}
            
        if trueC in table[predictedC]:
            table[predictedC][trueC] += 1
        else:
            table[predictedC][trueC] = 1
    
    total = len(cData)     
    for j in table:  
        for k in table[j]:
            table[j][k] = (float)(table[j][k])/total
    
    return table
        
                
        
        
        
        
        
        