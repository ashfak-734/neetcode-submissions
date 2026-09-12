class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        if len(strs) == 1:
            return strs[0]
    
        r = 0
        isset = True 
        while isset:
            for i in range(len(strs)-1):
                word = strs[i]

                if r == len(word) or r == len(strs[i + 1]): 
                    isset = False 
                    break

                if word[r] != strs[i+1][r]:
                    isset = False
                    break

            if not isset:
                break
            
            longest = strs[0][:r+1]
                    
            r += 1


            

        return longest
                    


         





        