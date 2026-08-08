class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         r = 0  #4
         l = 0  #2
         my_set = set()
         longest =  0  # 3

         while r<len(s):  
            if s[r] not in my_set:
                my_set.add(s[r]) 
                r += 1
                lenght = (r-l)
                longest = max(longest,lenght)
            else: 
                my_set.remove(s[l])
                l += 1 
                
           
         return longest
            # {y , z}
            #" z x y z x y z"
            #          |
            #      |
        