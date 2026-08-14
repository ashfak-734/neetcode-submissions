class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        code1 = [0]*26
        code2 = [0]*26

        l = 0
        if len(s1) > len(s2):
            return False

        for c in s1:
            code1[ord(c)-ord("a")] += 1

        
        for i in range(len(s1)):
            code2[ord(s2[i])- ord("a")] += 1

        if code1 == code2:
            return True 

        for i in range(len(s1),len(s2)):
            code2[ord(s2[i])- ord("a")] += 1
            code2[ord(s2[l])- ord("a")] -= 1
            l += 1
            if code1 == code2:
                return True 

        return False



           


        
            

            


        