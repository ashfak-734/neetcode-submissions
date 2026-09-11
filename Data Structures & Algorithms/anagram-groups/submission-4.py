class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dic = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in my_dic:
                my_dic[sorted_string] = []
                
            my_dic[sorted_string].append(s)

        
        result = list(my_dic.values())

        return result

       

           






        
