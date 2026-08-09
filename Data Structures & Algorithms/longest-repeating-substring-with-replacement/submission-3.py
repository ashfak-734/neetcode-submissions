class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
    
        l = 0
        freq = [0]*26 
        longest = 0

        for r in range(len(s)):
            freq[ord(s[r])-ord("A")] += 1
            while (r-l)+1-max(freq) > k:
                freq[ord(s[l])-ord("A")] -= 1
                l += 1

            lenght = (r-l)+1
            longest = max(lenght,longest)

        return longest

        




        