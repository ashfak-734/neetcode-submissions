class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
           count[i] = count.get(i,0) + 1

        

        buckets = [[] for _ in range(len(nums)+1)]

        for key,values in count.items():
             buckets[values].append(key)
        result = []

        for i in range(len(nums),-1,-1):
            for ele in buckets[i]:
                result.append(ele)

                if len(result) == k:
                    return result 
                            



            



        
                


        

        



        
           
           
       