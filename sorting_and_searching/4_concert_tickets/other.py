# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:42:57 2020
 
@author: macal
"""
 
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
 
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]: 
          hi = mid
        else: 
          lo = mid+1
    return lo
  
 
tickets, customers = tuple([int(x) for x in input().split()])
pricelist = sorted([int(x) for x in input().split()])
paylist = [int(x) for x in input().split()]
soldlist = list(range(tickets+1))
result = [-1]*customers
 
for i in range(customers):
  x = y = bisect_right(pricelist, paylist[i])

  while soldlist[x] != x:
    # print(x, soldlist[x])
    # sold already, check left to find available
    x = soldlist[x] # x = soldlist[x] faster than x = x -1
  print('before: %d %d', x, y)
  while y != x:
    # 
    tmp = soldlist[y]
    soldlist[y] = x
    y = tmp

  print(x, y, soldlist, result, pricelist)
    
  if x > 0:
    soldlist[x] = x-1
    result[i] = pricelist[x-1]  
    
print(soldlist)
print(*result, sep='\n')
# unpack the sequence with the star operator (*) and let print() handle type casting  
  
  
  
  
