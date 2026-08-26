class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        result  = [0]*len(t)
        stack = []

        for idx,temp in enumerate(t):
            while stack and  temp > stack[-1][1]:
               i,v = stack.pop()
               result[i] = idx-i
            
            stack.append((idx,temp))

        return result 
              
               
          
        