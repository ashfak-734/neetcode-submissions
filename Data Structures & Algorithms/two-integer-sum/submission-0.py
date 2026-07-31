class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        dic = {}
        """
        {3 : 0,
        }

        """
        for i in range(len(nums)):  #5 
            compliment = target - nums[i]  #2
            if compliment not in dic:
                dic[nums[i]] = i
            else:
                output.append(dic[compliment])
                output.append(i)  
                del dic[compliment]

           
        

        return output


        