class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        code_s1 = [0]*26
        code_s2 = [0]*26
         
        
        if len(s1) > len(s2):
            return False
            
        for i in s1:
            code_s1[ord(i)-ord("a")] += 1

        for i in range(len(s1)):
            c = s2[i]
            code_s2[ord(c)-ord("a")] += 1

        if code_s1 == code_s2:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            code_s2[ord(s2[r])-ord("a")] += 1

            if (r-l+1) > len(s1):
                code_s2[ord(s2[l])-ord("a")] -= 1
                l += 1

            if code_s2 == code_s1:
                return True 

        return False 





        