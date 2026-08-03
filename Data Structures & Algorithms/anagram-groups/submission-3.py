class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       dic = {}
       
       for word in strs:  # "act" 
          unique_code = [0]*26      
          for c in word: 
             unique_code[ord(c)- ord("a")] += 1
          
          unique_code = tuple(unique_code)

          if unique_code not in dic:
              dic[unique_code] = []

          dic[unique_code].append(word)

       return list(dic.values())
             
        

           






        
