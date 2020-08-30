# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:12:41 2019

@author: GOVIND A M
"""

n = 16
#data = [[1,2,'b'],[2,3,'r'],[3,4,'r'],[4,5,'b']]
#data = [[7,3,'r'],[1,2,'r'],[1,3,'r'],[1,4,'r'],[3,5,'r'],[3,6,'r']]
tree = [0 for _ in range(n+1)]
sett = []
data = [[1, 2, 'b'], [2, 3, 'b'], [3, 4, 'b'], [3, 5, 'b'], [3, 6, 'b'], [2, 7, 'r'], [7, 15, 'b'], [15, 14, 'b'], [15, 13, 'b'], [7, 12, 'r'], [7, 8, 'r'], [8, 16, 'r'], [16, 11, 'b'], [16, 10, 'b'], [8, 9, 'r']]

class node:
  def __init__(self,index,rc,bc):
    self.index = index
    self.rc = rc
    self.bc = bc
    self.setID = None
  
  def __repr__(self):
    return f'{self.index} {self.setID}'

class rbset:
  def __init__(self,noe,colour,setID):
    self.setID = setID
    self.noe = noe
    self.colour = colour
    sett.append(self)
    
def cleanTree(parent):
  global tree
  for c in parent.rc:
    for i in range(len(c.rc)):
      if c.rc[i].index==parent.index:
        del c.rc[i]
        break
    if len(c.rc)+len(c.bc)>0:
      cleanTree(c)
  for nbr in parent.bc:
    for j in range(len(nbr.bc)):
      if nbr.bc[j].index==parent.index:
        del nbr.bc[j]
        break
    if len(nbr.bc)+len(nbr.rc)>0:
      cleanTree(nbr)

def classify(parent,gp):
  global sett
  if  parent.setID==None:
    if len(parent.bc)>0:
      parent.setID = rbset(1,'b',len(sett)).setID
    else:
      if sett[gp.setID].colour=='b':
        parent.setID = rbset(1,'r',len(sett)).setID
      else:
        parent.setID = gp.setID
        sett[parent.setID].noe+=1
  if sett[parent.setID].colour=='b':
    sett[parent.setID].noe = sett[parent.setID].noe+len(parent.bc)
    for b in parent.bc:
      b.setID = parent.setID
      classify(b,parent)
    for r in parent.rc:
      classify(r,parent)
  else:
    for red in parent.rc:
      classify(red,parent)



def nc23(n):
  global nob
  c2 = n*(n-1)//2
  return c2+(c2*(n-2)//3)*nob

for con in data:
  if tree[con[0]]==0:
    tree[con[0]] = node(con[0],[],[])
  if tree[con[1]]==0:
    tree[con[1]] = node(con[1],[],[])
  if con[2]=='b':
    tree[con[0]].bc.append(tree[con[1]])
    tree[con[1]].bc.append(tree[con[0]])
  else:
    tree[con[0]].rc.append(tree[con[1]])
    tree[con[1]].rc.append(tree[con[0]])

cleanTree(tree[1])
parent = tree[1]
gp = node(0,[],[])
gp.setID = rbset(0,'b',0).setID
parent.setID = rbset(1,'b',len(sett)).setID if len(parent.bc)>0 else None
classify(parent,gp)

c_sum = 0
result = 0
nob = 0
for i in range(1,len(sett)):
  if sett[i].colour=='b':
    nob = nob+sett[i].noe
    
for i in range(1,len(sett)-2):
  c_sum = c_sum+sett[i].noe
  if sett[i].colour=='r':
    result = result+(c_sum*sett[i+2].noe*sett[i+1].noe)+nc23(sett[i].noe)
  else:
    result = result+(c_sum*sett[i+2].noe*sett[i+1].noe

if sett[-1].colour=='r':
  pass

#if sett[-1].colour=='r' :
#  result = result+nc23(sett[-1].noe)
#if sett[-2].colour=='r':
#  result = result+nc23(sett[-2].noe)

  
