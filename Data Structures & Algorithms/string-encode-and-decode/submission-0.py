class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_value = ""
        for i in range(len(strs)):
            encoded_value += str(len(strs[i])) + "#" + strs[i]

        return encoded_value

        
    def decode(self, s: str) -> List[str]:
        "4#Hello5#World"
        i = 0 #0
        result = []
        while i < len(s):
            j = i #0
            while s[j] != "#":
                j +=1 
            lenght = int(s[i:j])
            result.append(s[j+1: j+1+lenght])
            i = j+1+lenght

        return result






      

        
