# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:45:43 2019

@author: MLG1KOR
"""

arr = [[7,3],[1,2],[1,3],[1,4],[3,5],[3,6],[3,7]]
nob = 0
bch = []

class node:
  
  def __init__(index,nbrs):
    self.index = index
    self.nbrs = nbrs
    self.branchID = None
  
def growTree(arr,n):
  tree = [0 for _ in range(n+1)]
  for con in arr:
    if con[0]!=0:
      node0 = node(con[0],[])
    else:
      node0 = tree[con[0]]
    if con[1]!=0:
      node1 = node(con[1],[])
    else:
      node1 = tree[con[1]]
    node0.nbrs.append(node1)
    node1.nbrs.append(node0)

def branches(parent):
  global nob,bch
  


parent = tree[1]
parent.branchID = 1
