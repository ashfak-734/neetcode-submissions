class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        my_dic = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]

            if difference not in my_dic:
                my_dic[numbers[i]] = i+1
                continue
            
            return [my_dic[difference], i+1]

            

        