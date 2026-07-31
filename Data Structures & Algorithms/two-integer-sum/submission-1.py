class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        output = []

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment not in dic:
                dic[nums[i]] = i
            else:
                output.append(dic[compliment])
                output.append(i)
                
        return output

        



        