class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i))+"#"+i

        return encode

    def decode(self, s: str) -> List[str]:
        #  5#Hello5#World
        #         |
        #         |
        r,l = 0,0
        result = []
        while r<len(s):
            while s[r] != "#":
                r += 1

            lenght = int(s[l:r])
            l = r+1
            result.append(s[l:r+lenght+1])
            r = r+lenght+1
            l = r

        return result 




