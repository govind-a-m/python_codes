# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:07:12 2019

@author: GOVIND A M
"""
import functools

def generateMatrix(row):
  matrix = [[0 for _ in range(row+1)] for _ in range(2*row)]
  matrix[0] = [1 for i in range(row)]+[0]
  for i in range(1,row+1):
    matrix[i][row] = 1
  for i in range(1,2*row):
    for j in range(row-1,-1,-1):
      matrix[i][j] = matrix[i-1][j]+matrix[i][j+1]
  return matrix

@functools.lru_cache
def recurMatrix(na,nb):
  if 


t = [6]
mx = (max(t)+1)//2
matrix = generateMatrix(mx)
for i in range(len(t)):
  if t[i]==1:
    print(1)
  else:
    if t[i]%2==0:
      na = t[i]//2
      nb = t[i]
      print(pow(matrix[nb-1][mx-na],2))
    else:
      na1 = (t[i]+1)//2
      na2 = (t[i]-1)//2
      nb = t[i]
      print(matrix[nb-1][mx-na1]*matrix[nb-1][mx-na2])
      