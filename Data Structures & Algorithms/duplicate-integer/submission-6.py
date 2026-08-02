class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_dic = {}

        for i in range(len(nums)):
            if nums[i] not in my_dic:
                my_dic[nums[i]] = 1
            else:
                my_dic[nums[i]] += 1

        result = list(my_dic.values())

        for i in result:
           if i > 1:
             return True
         
        return False






        

    

        

    