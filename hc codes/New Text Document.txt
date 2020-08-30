'''
please check problem statement at 
https://www.hackerrank.com/challenges/morgan-and-a-string
'''

import math
import os
import random
import re
import sys

def morganAndString(a, b):
  ai = 0
  bi = 0
  s = ''
  lena = len(a)
  lenb = len(b)
  try:    
    while True:
      if a[ai] > b[bi] :
        s = s+b[bi]
        bi+=1
      elif b[bi] > a[ai]:
        s = s+a[ai]
        ai+=1
      else :
        sai = ai+1
        sbi = bi+1
        while (a[sai]==b[sbi]):
          if a[sai]>=a[ai]:
            break
          sai+=1
          sbi+=1
          if sai==lena:
            break
          if sbi==lenb:
            break
        if sai==lena:
          if sbi==lenb:
            s = s+a[ai:sai]+b[bi:sbi]
            ai = sai
            bi = sbi
          else :
            if a[ai]<b[sbi]:
              s = s+a[ai:sai]+b[bi:sbi]
              ai = sai
              bi = sbi
            else:
              s = s+b[bi:sbi]
              bi = sbi
        else:
          if sbi==lenb:
            if b[bi]<a[sai]:
              s = s+a[ai:sai]+b[bi:sbi]
              ai = sai
              bi = sbi
            else:
              s = s+a[ai:sai]
              ai = sai
          else:
            if a[sai]!=b[sbi]:
              if a[sai]<b[sbi]:
                if a[ai]<a[sai]:
                  s = s+a[ai:sai]+b[bi:sbi]
                  a = sai
                  b = sbi
                else :
                  s = s+a[ai:sai]
                  ai = sai
              else:
                if b[bi]<b[sbi]:
                  s = s+b[bi:sbi]+a[ai:sai]
                  a = sai
                  b = sbi
                else :
                  s = s+b[bi:sbi]
                  bi = sbi
            else:
              if a[sai]==a[ai]:
                if (lena-sai)<(lenb-sbi):
                    if (a[sai:]+'a')<=b[sbi:]:
                        s = s+a[ai:sai]
                        ai = sai
                    else:
                        s = s+b[bi:sbi]
                        bi = sbi
                else:
                    if (b[sbi:]+'a')<=a[sai:]:
                        s = s+b[bi:sbi]
                        bi = sbi
                    else:
                        s = s+a[ai:sai]
                        ai = sai
                    
              else:
                s = s+a[ai:sai]+b[bi:sbi]
                ai = sai
                bi = sbi
   
  except :
    if ai==lena:
      if bi==lenb:
        pass
      else:
        s = s+b[bi:]
    else:
      if bi==lenb:
        s = s+a[ai:]
      else:
        if sai==lena:
          if sbi==lenb:
            s = s+a[ai]+b[bi]
          else:
            while (sbi<lenb):
              if b[sbi]>a[sai-1]:
                break
              sbi+=1
            s = s+b[bi:sbi]+a[sai-1]+b[sbi:]
        else:
          while sai<lena:
            if a[sai]>b[sbi-1]:
              break
            sai+=1
          s = s+a[ai:sai]+b[sbi-1]+a[sai:]
    return s 




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
