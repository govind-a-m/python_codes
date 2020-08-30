# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:45:43 2019

@author: MLG1KOR
"""
import bisect

arr = [[7,3],[1,2],[1,3],[1,4],[3,5],[3,6]]
#arr = [[2,3],[2,4],[2,5],[1,6],[6,12],[12,13],[12,14],[6,7],[7,11],[7,8],[8,9],[8,10],[14,2]]

class node:
  def __init__(self,index,nbrs):
    self.index = index
    self.nbrs = nbrs
    self.branchID = None
    self.depth = None
  
  def __repr__(self):
    return f'{self.index} {self.branchID} {self.depth}'
  
def cleanTree(parent):
  global tree
  for nbr in parent.nbrs:
    for i in range(len(nbr.nbrs)):
      if nbr.nbrs[i].index==parent.index:
        del nbr.nbrs[i]
        break
    if len(nbr.nbrs)>0:
      cleanTree(nbr)
  
def growTree(arr,n):
  tree = [0 for _ in range(n+1)]
  for con in arr:
    if tree[con[0]]==0:
      tree[con[0]] = node(con[0],[])
    if tree[con[1]]==0:
      tree[con[1]] = node(con[1],[])
    tree[con[0]].nbrs.append(tree[con[1]])
    tree[con[1]].nbrs.append(tree[con[0]])      
  return tree

def branches(parent,depth,start):
  global bch
  for i,nbr in enumerate(parent.nbrs):
    print(i,nbr)
    if i!=0:
      bch.append([])
    nbr.branchID = len(bch)-1
    nbr.depth = depth+1
    end = len(bch)
    if len(nbr.nbrs)>0:
      branches(nbr,depth+1,end-1)
    ap = [depth,len(bch)-end+1]
    for k in range(start,end-1):
      bch[k].append(ap)
      print(k,bch[k])

def flattenIndex():
  global bch
  idx_li = []
  for bc in bch:
    idx = 0
    li = []
    for i in range(len(bc)):
      idx = idx+bc[i][1]
      li.append(idx)
    idx_li.append(li)
  return idx_li

def KsC(li):
  global bch,tree,bchIndex
  result = 0
  for i in range(len(li)-1):
    for j in range(i+1,len(li)):
      if tree[li[i]].branchID!=tree[li[j]].branchID:
        idx = bisect.bisect_left(bchIndex[min(tree[li[i]].branchID,tree[li[j]].branchID)],abs(tree[li[i]].branchID-tree[li[j]].branchID))
        sep_depth = bch[min(tree[li[i]].branchID,tree[li[j]].branchID)][idx][0]
        distance = abs(sep_depth-tree[li[i]].depth)+abs(sep_depth-tree[li[j]].depth)
        result = result+li[i]*li[j]*distance
      else:
        distance = abs(tree[li[i]].depth-tree[li[j]].depth)
        result = result+li[i]*li[j]*distance
      print(li[i],li[j],distance)
  return result

bch = [[]]
tree = growTree(arr,7)
cleanTree(tree[1])
tree[1].depth = 0
tree[1].branchID = 0
branches(tree[1],0,0)
bchIndex = flattenIndex()
li = [1,2,3,4,5,6,7]
print(KsC(li))

# =============================================================================
# def KsC(li,bch,tree):
#   result = 0
#   for i in range(len(li)-1):
#     for j in range(i+1,len(li)):
#       if tree[li[i]].branchID!=tree[li[j]].branchID:
#         sep_depth = bch[min(tree[li[i]].branchID,tree[li[j]].branchID)][abs(tree[li[i]].branchID-tree[li[j]].branchID)-1]
#         distance = abs(sep_depth-tree[li[i]].depth)+abs(sep_depth-tree[li[j]].depth)
#         result = result+li[i]*li[j]*distance
#       else:
#         distance = abs(tree[li[i]].depth-tree[li[j]].depth)
#         result = result+li[i]*li[j]*distance
#       print(li[i],li[j],distance)
#   return result
# =============================================================================
