class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(",
                   "]":"[",
                   "}":"{",
                   }

        stack = []

        for c in s:
           if c not in hashmap:
              stack.append(c)
           else:
              if stack:
                 popped = stack.pop()
                 if popped != hashmap[c]:
                   return False
              else:
                 return False
    
        if stack:
           return False

        return True 
           
              
              

        
        
        