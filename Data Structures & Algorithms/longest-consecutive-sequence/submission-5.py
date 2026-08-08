class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 not in s:
                lenght = 1
                next_num = i+1
                while next_num in s:
                     next_num += 1
                     lenght += 1

                longest = max(lenght,longest)

        return longest 




        


       
           

        




        