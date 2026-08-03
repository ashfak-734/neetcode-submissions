class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1

        """
        {1:1,
         2:2,
         3:3
        }
        """
        buckets = [[] for i in range(len(nums)+1)]
        for freq in range(len(nums)+1):
            for key,val in count.items():
                if val == freq:
                    buckets[freq].append(key)

        result = []
        for freq in range(len(nums),-1 ,-1):
            if buckets[freq]:
                for i in buckets[freq]:
                    result.append(i)
                    if len(result) == k:
                        return result
            

            



        
                


        

        



        
           
           
       