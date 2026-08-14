class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ADOBECODEBANC  ABC
        freq = {}
        for i in t:
            freq[i] = freq.get(i,0) + 1

        l = 0

        dic = {}

        have,need = 0,len(freq)

        result = []

        res,reslen = [-1,-1] , float("infinity")

        for r in range(len(s)):
            c = s[r]
        
            dic[c] = dic.get(c,0) + 1

            if c in freq and dic[c] == freq[c]:
                  have += 1

            while have == need:
                if r-l+1 < reslen:
                   res = l,r
                   reslen = r-l+1

                dic[s[l]] -= 1
                if s[l] in freq and dic[s[l]] < freq[s[l]]:
                    have -= 1

                l += 1

        l,r = res

        return s[l:r+1] if reslen != float("infinity") else ""









        