class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for index,string in enumerate(strs):
            sorted_string = "".join(sorted(strs[index]))

            if sorted_string not in group:
                group[sorted_string] = [string]
            else:
                group[sorted_string].append(string)

        return list(group.values())



        
        