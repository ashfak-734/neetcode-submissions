class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        code_s1 = [0]*26
        code_s2 = [0]*26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            code_s1[ord(s1[i])- ord("a")] += 1
            code_s2[ord(s2[i])- ord("a")] += 1

        if code_s1 == code_s2:
            return True

        for i in range(len(s1),len(s2)):
             code_s2[ord(s2[i])- ord("a")] += 1
             code_s2[ord(s2[i-len(s1)])- ord("a")] -= 1

             if code_s1 == code_s2:
                return True 

        return False


            

            


        