# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:53:01 2019

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
      print(s[v[0]:])
      yield v[0]

def sumof_nterms(start,end):
  return (end-start+1)*(start+end)//2


s= 'nvzjkcahjwlhmdiuobjdwbanmvrtadopapbktdtezellktgywrdstdhhayaadqrdhspavjgxprk'
n = 2071
lens = len(s)
lcp = [0]*lens
suffix = suffix_array_ManberMyers(s, range(lens), 1)
pa = ''
cnt = 0
idx = 0
while cnt<n:
  cmn = lcp[idx]
  idx = next(suffix)
  if s[idx]!=pa:
    cmn = 0
  pa = s[idx]
  nos = lens-idx-cmn
  sm = (nos*(2*(cmn+1)+(nos-1))//2)
  if n<=(cnt+sm):
    start = cmn+1
    end = start+nos-1
    while True:
      print(start,end)
      if (end-start+1)%2==0:
        mid = (start+end)//2
        sm = sumof_nterms(cmn+1,mid)
        if cnt+sm-mid<n<=cnt+sm:
          c = s[idx+mid-cnt-sm+n-1]
          cnt = n
          break
        elif n>(cnt+sm):
          start = mid+1
        else:
          end = mid-1
      else:
        mid = (start+end+1)//2
        sm = sumof_nterms(cmn+1,mid)
        if cnt+sm-mid<n<=cnt+sm:
          c = s[idx+mid-cnt-sm+n-1]
          cnt = n
          break
        elif n>(cnt+sm):
          start = mid+1
        else:
          end = mid-1
  print(cnt)
  cnt = cnt+sm    
print(c)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  