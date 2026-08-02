class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for char in s:
            count[char] = count.get(char , 0) + 1

        for char in t:
            count[char] = count.get(char , 0) - 1

        result = list(count.values())

        for i in result:
            if i !=  0:
                return False

        return True

        
      
       
       
 
             
             