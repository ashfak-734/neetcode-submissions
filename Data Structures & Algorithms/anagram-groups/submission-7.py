class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            code = [0]*26
            for c in s:
                code[ord("a")-ord(c)] += 1

            code = tuple(code)
            
            if code not in dic:
               dic[code] = []

            dic[code].append(s)

        return [ _ for _ in dic.values()]


               





        