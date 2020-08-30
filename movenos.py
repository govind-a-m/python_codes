# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:48:47 2019

@author: GOVIND A M
"""

arr = [1,2,3,4,5,6,7,8,9,10]
sects = [[1,10]]
queries = [[1,2,4],[2,3,5],[1,5,10],[1,4,8]]

def get_elements(nerq):
  global li
  
for q  in queries:
  cnt = 0
  i = 0
  while cnt+sects[i][1]-sects[i][0]+1<q[1]:
    i+=1
  li = []
  if cnt+1==q[1]:
    noe = sects[i][1]-sects[i][0]+1 
    if noe==q[2]-q[1]+1:
      li.append(sects.pop(i))
    elif noe<q[2]-q[1]+1:
      li.append(sects.pop(i))
      get_elements(q[2]-q[1]+1-noe)
    else:
      li.append([sects[i][0],sects[i][0]+q[2]-q[1]])
      sects[i] = [sects[i][0]+q[2]-q[1]+1,sects[i][1]]
