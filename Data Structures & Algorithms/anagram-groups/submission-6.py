class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for i in strs:
            code = [0]*26

            for c in i:
                code[ord(c)- ord("a")] += 1

            code = tuple(code)

            if code not in d:
                d[code] = []

            d[code].append(i)


        result = list(d.values())

        return result

           






        
