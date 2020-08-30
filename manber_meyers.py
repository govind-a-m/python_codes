# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:50:57 2019

@author: MLG1KOR
"""

from collections import defaultdict

def suffix_array_ManberMyers(s, bucket, order):
  global lcp
  d = defaultdict(list)
  for i in bucket:
    key = s[i + order-1:i + order]
    d[key].append(i)
  for k, v in sorted(d.items()):
    if len(v) > 1:
      for idx in v:
        lcp[idx]+=1
      yield from suffix_array_ManberMyers(s, v,order+1)
    else:
      yield v[0]
  lcp[v[0]] = lcp[v[0]]-1

def gen_delay():
  pidx = 0
  for idx in suffix:
    yield (idx,lcp[pidx])
    pidx = idx

    
s= 'nvzjkcahjwlhmdiuobjdwbanmvrtadopapbktdtezellktgywrdstdhhayaadqrdhspavjgxprk'
#s = 'banana'
n = 2071
lens = len(s)
lcp = [0]*lens
suffix = suffix_array_ManberMyers(s, range(lens), 1)
delay = gen_delay()
for index,cmn in delay:
  print(s[index:],cmn)
  