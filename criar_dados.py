# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:37:51 2019

@author: rotc_
"""
import csv
import numpy as np
import math

data = []

with open('quadra.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';')
  for row in spamreader:
    data.append(np.array(row[1:7]).astype(int))

data = np.array(data)

data_prep = []

i = 1

def acharMedianaData(data, maximun, filtro):
    a = np.count_nonzero(np.where(data[:maximun] == filtro))
    if(math.isnan(a)):
        return 0
    else:
        return a

def acharCountData(data, maximun, filtro):
    a = np.nanmean(np.where(data[:maximun] == filtro))
    if(math.isnan(a)):
        return 0
    else:
        return a

def acharMedianData(data, maximun, filtro):
    a = np.median(np.where(data[:maximun] == filtro))
    if(math.isnan(a)):
        return 0
    else:
        return a

def acharAverageData(data, maximun, filtro):
    a = np.average(np.where(data[:maximun] == filtro))
    if(math.isnan(a)):
        return 0
    else:
        return a
    
target  = 152    
    
while i < data.shape[0]+1:
  d = 0;
  if(i <= target):
    d = 0
  else:
    d = i-target
  
  y = 0
  linha = [[[] for x in range(1,41)]for x in range(1,61)]
  
  while(y < 60):
    z = 0
    while(z < 10):
        linha[y][z] = acharMedianaData(data[d:i], int(i * (z / 100))+1, y)
        z += 1

    while(z < 20):
        linha[y][z] = acharCountData(data[d:i], int(i * (z / 100))+1, y)
        z += 1
    while(z < 30):
        linha[y][z] = acharMedianData(data[d:i], int(i * (z / 100))+1, y)
        z += 1
    while(z < 40):
        linha[y][z] = acharAverageData(data[d:i], int(i * (z / 100))+1, y)
        z += 1
    y += 1
  data_prep.append(linha)
  i += 1

data_prep = np.array(data_prep)