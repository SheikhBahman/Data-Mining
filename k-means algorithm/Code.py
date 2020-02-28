# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:10:02 2019

@author: Bahman
"""
import math
import random
import numpy as np

k = 3

def distance(point1, point2):    
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2)

def center(data):
    centers = []
    for i in range(len(data)):
        X = 0.0
        Y = 0.0
        
        #should try a several time until don't have an empty group
        for item in data[i]:
            X += item[0]
            Y += item[1]
        centers.append([X / len(data[i]), Y / len(data[i])])
        
            
    return centers

def errorCal(new, old):
    return np.sum(np.array(new) - np.array(old))
        

    
    
    
with open('data.txt','r') as f:
    data = []
    for line in f:
        line = line.strip()
        x,y = line.split(',')
        data.append([float(x), float(y)])

    maxX = max([point[0] for point in data])    
    minX = min([point[0] for point in data])    
    
    maxY = max([point[1] for point in data])    
    minY = min([point[1] for point in data])  
    
    centers = []
    oldCenters = [0] * k
    pointsCLusterID = {}
    
    for i in range(k):
        pointsCLusterID[i] = []
        centers.append([random.uniform(minX, maxX), random.uniform(minY, maxY)])
    
    error = 10.0
    while error > 0.001:
        pointsCLusterID = {key: [] for key in pointsCLusterID.keys()}
        for point in data:
            distanceP = []
            for i in range(k):
                distanceP.append(distance(centers[i], point))            
            pointsCLusterID[distanceP.index(min(distanceP))].append(point)
        oldCenters = centers.copy()
        
        centers = center(pointsCLusterID)
        error  = errorCal(centers, oldCenters)
    
    listCluster = []
    for item in data:
        for i in range(k):
            if item in pointsCLusterID[i]:
                listCluster.append(i)
   
    with open("results.txt", "w") as clusterR:
        for i in range(len(data)):
            print(str(i)," ", str(listCluster[i]), file=clusterR)
        clusterR.close()
                
        
           
            

        
