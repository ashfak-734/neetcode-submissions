class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #pwwkew
        #  |
        # |
        #{w}
        # 2
        l,r = 0,0
        my_set = set()
        longest = 0

        while r<len(s):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            longest = max(longest,r-l+1)
            r += 1

        return longest


        