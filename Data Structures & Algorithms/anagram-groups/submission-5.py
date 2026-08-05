class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dic = {} 

        for s in strs:
            code = [0]*26
            for c in s:
               code[ord(c)- ord("a")] += 1

            code = tuple(code)

            if code not in my_dic:
                my_dic[code] = []

            my_dic[code].append(s)

        
        result = list(my_dic.values())

        return result

       

           






        
