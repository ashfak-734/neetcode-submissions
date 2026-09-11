class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s="aaaaaaaaaaaabbbbbcdd"   t="abcdd"               
        #                    |
        #               |

        count_s = {}
        count_t = {}

        for i in t:
            count_t[i] = count_t.get(i,0)+1
        
        have = 0
        need = len(count_t)
        l = 0
        reslen = float("inf")
        result = [0,0] 
        for r in range(len(s)):
            c = s[r]

            count_s[c] = count_s.get(c,0)+1

            if c in count_t and  count_t[c] == count_s[c]:
                have += 1

            while have==need:
                if r - l + 1 < reslen:
                   reslen = r - l + 1
                   result = [l, r]
                
                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -=1
                
                l += 1
               

        l,r = result

        return s[l:r+1] if reslen != float("inf") else ""


