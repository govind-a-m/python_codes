# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:19:43 2019

@author: GOVIND A M
"""
import sys
sys.setrecursionlimit(10**5)
with open(r'C:\Users\GOVIND A M\Desktop\ip.txt','r') as f:
  n,q = [int(x) for x in f.readline().split(' ')]
  arr = []
  for i in range(n-1):
    arr.append([int(x) for x in f.readline().split(' ')])
  li = []
  for i in range(q):
    f.readline()
    li.append([int(x) for x in f.readline().split(' ')])

class node:
  def __init__(self,index,nbrs):
    self.index = index
    self.nbrs = nbrs
    self.branchID = None
    self.depth = None

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
    if i!=0:
      bch.append([])
    nbr.branchID = len(bch)-1
    nbr.depth = depth+1
    end = len(bch)
    if len(nbr.nbrs)>0:
      branches(nbr,depth+1,end-1)
    ap = [depth for _ in range(end-1,len(bch))]
    for k in range(start,end-1):
      bch[k] = bch[k]+ap

def KsC(li):
  global bch,tree
  result = 0
  for i in range(len(li)-1):
    for j in range(i+1,len(li)):
      if tree[li[i]].branchID!=tree[li[j]].branchID:
        sep_depth = bch[min(tree[li[i]].branchID,tree[li[j]].branchID)][abs(tree[li[i]].branchID-tree[li[j]].branchID)-1]
        distance = abs(sep_depth-tree[li[i]].depth)+abs(sep_depth-tree[li[j]].depth)
        result = result+li[i]*li[j]*distance
      else:
        distance = abs(tree[li[i]].depth-tree[li[j]].depth)
        result = result+li[i]*li[j]*distance
  return result


def cleanTree(parent):
  global tree
  for nbr in parent.nbrs:
    for i in range(len(nbr.nbrs)):
      if nbr.nbrs[i].index==parent.index:
        del nbr.nbrs[i]
        break
    if len(nbr.nbrs)>0:
      cleanTree(nbr)
  return tree

bch = [[]]
tree = growTree(arr,n)
cleanTree(tree[1])
tree[1].depth = 0
tree[1].branchID = 0
branches(tree[1],0,0)
with open('out.txt','w') as f:
  for t in li:
    f.write(str(KsC(t)%1000000007))
    f.write('\n')
