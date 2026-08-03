class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       dic = {}
       for i in range(len(strs)):
          sorted_string = "".join(sorted(strs[i]))
          if sorted_string not in dic:
             dic[sorted_string] = []
          dic[sorted_string].append(strs[i])

       return list(dic.values())




        
