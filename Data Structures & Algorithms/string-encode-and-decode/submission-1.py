class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + "#" + string
            
        return encode


    
    def decode(self, s: str) -> List[str]:

        # "4#Hello5#world"
        i = 0  #0
        j = 0 #1
        result = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            
            lenght = int(s[i:j])
            result.append(s[j+1: j+ 1 +lenght])
            i =  j+ 1 +lenght
            j = i

        return result


            



