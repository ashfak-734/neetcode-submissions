class Solution:
    def isValid(self, s: str) -> bool:
      hashmap  = {")":"(","}":"{","]":"["}

      stack = []

      for c in s:
         if c in hashmap:
            if not stack:
               return False
            popped = stack.pop()
            if hashmap[c] != popped:
                return False
         else:
            stack.append(c)


      return not stack 


      
         
       
       
        
        
        