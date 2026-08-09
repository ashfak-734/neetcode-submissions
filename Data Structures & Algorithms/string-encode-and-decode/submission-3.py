class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i

        return encode


    def decode(self, s: str) -> List[str]:
        #   5#Hello5#World
        i = 0
        j = 0 
        result = []
        while i < len(s):

            while s[j] != "#":
                j += 1 
            lenght = int(s[i:j])

            result.append(s[j+1: j + lenght + 1])
            j = j + lenght + 1
            i = j

        return result


