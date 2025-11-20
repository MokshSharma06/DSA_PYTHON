#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
         n = len(arr)
         dq = deque()
         result = [ ]
         for i in range(n):
             if arr[i]<0:
                 dq.append(i)
                 
             if i>=k-1:
                 if dq:
                     result.append( arr[dq[0]])
                 else:
                    result.append(0)
                 left_index = i-k+1
                 
                 if dq and dq[0]==left_index:
                     dq.popleft()
                    
         return result
                    
                    
                    
