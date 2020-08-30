'''
Please check problem statement at
https://www.hackerrank.com/challenges/no-prefix-set
solution is incomplete
'''

class Node:
  cnt = 0
  def __init__(self,ID,value,sibling,children,istail):
    self.ID = ID
    self.value = value
    self.sibling = sibling
    self.__class__.cnt+=1
    self.children = children
    self.istail = istail
    
def CreateChild(parent,value,istail):
  for child in parent.children:
    if child.value==value:
      child.sibling+=1
      child.istail = True if istail else child.istail
      return (child,child.istail)
  n = Node(Node.cnt,value,1,[],istail)
  parent.children.append(n)
  return (n,False)
    
def NoPrefix():
  global prev_count,li,idList
  index = 0
  while True:
    if prev_count-Node.cnt!=0:
      prev_count = Node.cnt
      for i in range(len(li)):
        parent = idList[i]
        if parent.sibling>1:
          if index<len(li[i]):
            idList[i],brk = CreateChild(parent,li[i][index],index==len(li[i])-1)
            if brk:
              print('BAD SET')
              print(li[i])
              return 
      index = index+1
    else:
      print('GOOD SET')
      return



lines = int(input().strip())
li = []
for _ in range(lines):
    li.append(input().strip())
n = Node(0,'',10,[],False)
idList = [n for _ in li]
prev_count = -1
NoPrefix()

