class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" +  s
        return encode

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World"
        i = 0
        j = 0

        result = []
      
        while i < len(s):
            while s[j] != "#":
                j += 1

            lenght = int(s[i:j])

            result.append(s[j+1: j+1 + lenght])
            i = j+1 + lenght
            j = i

        return result







