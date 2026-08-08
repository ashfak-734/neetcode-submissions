class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       d = {}

       for i in nums:
          d[i] = d.get(i,0) + 1

       buckets = [[] for _ in range(len(nums) + 1)]

       for key,value in d.items():
           buckets[value].append(key)
    
       result = []
       for i in range(len(nums), -1 , -1):
            for e in buckets[i]:
                result.append(e)
                if len(result) == k:
                    return result 
           



            



        
                


        

        



        
           
           
       