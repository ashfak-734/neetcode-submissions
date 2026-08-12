class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        r = 0
        l = 0

        longest = 0


        while r<len(s):
            if s[r] not in sett:
                sett.add(s[r])
                longest = max(longest,r-l+1)
                r += 1
            else:
                sett.remove(s[l])
                l += 1

        return longest


            


        