# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:24:01 2019

@author: MLG1KOR
"""
from heapq import heappush, heappop

data = [[0,9],[10,4]]
data = sorted(data)
lend = len(data)
heap = []
time_taken = data[0][1]
time = data[0][1]+data[0][0]

def add_to_waitlist():
  global time,nof_ord,lend
  for i in range(nof_ord+1,lend):
    if data[i][0]<=time:
      continue
    return i-1
  return lend-1
  
nof_ord = 0
prev_nof = 0
total_ord = 1
while total_ord<lend:
  nof_ord = add_to_waitlist()
  for j in range(prev_nof+1,nof_ord+1):
    heappush(heap,[data[j][1],data[j][0]])
  if len(heap)>0:
    next_ord = heappop(heap)
  else:
    next_ord = [data[total_ord][1],data[total_ord][0]]
    nof_ord+=1
  time_taken = time_taken+time-next_ord[1]+next_ord[0]
  total_ord+=1
  prev_nof = nof_ord
  time =  time+next_ord[0]