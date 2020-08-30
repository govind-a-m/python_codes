# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:51:38 2019

@author: MLG1KOR
"""
n = 5
data = [[1,2,'b'],[2,3,'r'],[3,4,'r'],[4,5,'b']]

setmap = [-1 for _ in range(n+1)]

class rbset:
  def __init__(self,noe,colour):
    self.noe = noe
    self.parent_set = None
    self.colour = colour
    self.lastchild
    
  def add(self,node):
    self.noe+=1
    setmap[node] = self
  
  def __repr__(self):
    return f'{self.noe} {self.colour} {self.parent_set}'
  
redcon = []
b = []
r = []
for con in data:
  if con[2]=='b':
    if setmap[con[0]]!=-1:
      if setmap[con[1]]!=-1:
        setmap[con[0]].parent_set = setmap[con[1]]
      else:
        setmap[con[0]].add(con[1])
    else:
      if setmap[con[1]]!=-1:
        setmap[con[1]].add(con[0])
      else:
        setmap[con[0]]=setmap[con[1]] = rbset(2,'b')
        b.append(setmap[con[0]])
  else:
    redcon.append(con)

for con in redcon:
  if setmap[con[0]]!=-1:
    if setmap[con[1]]!=-1:
      if setmap[con[0]].colour==setmap[con[1]].colour=='r':
        setmap[con[0]].parent_set = setmap[con[1]]
    else:
      if setmap[con[0]].colour=='b':
        setmap[con[1]] = rbset(1,'r')
        r.append(setmap[con[1]])
      else:
        setmap[con[0]].add(con[1])
  else:
    if setmap[con[1]]!=-1:
      if setmap[con[1]].colour=='b':
        setmap[con[0]] = rbset(1,'r')
        r.append(setmap[con[0]])
      else:
        setmap[con[0]]=setmap[con[1]]=rbset(2,'r')
        r.append(setmap[con[0]])

for 