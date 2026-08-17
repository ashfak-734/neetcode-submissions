class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        code1 = [0]*26
        code2 = [0]*26 

        for c in s1:
            code1[ord(c)-ord("a")] += 1

        l = 0

        for r in range(len(s2)):

            code2[ord(s2[r])-ord("a")] += 1

            if r+1 >= len(s1):
                if code1 == code2:
                    return True 
                code2[ord(s2[l])-ord("a")] -= 1
                l += 1

        return False

        

        
            


       
           


        
            

            


        