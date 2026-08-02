class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in seen:
                seen[nums[i]] = i
            else:
                return [seen[difference] , i]

    



        



        