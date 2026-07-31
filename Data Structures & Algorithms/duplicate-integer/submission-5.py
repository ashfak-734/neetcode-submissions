class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
               dic[nums[i]] += 1
            else:
               dic[nums[i]] = 1
        """
        {1:1,
        2:1,
        3:2,
        }
        """
        for value in dic.values():
            if value > 1:
                return True
            
        return False

    

        

    