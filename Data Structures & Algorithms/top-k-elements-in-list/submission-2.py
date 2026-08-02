class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums)+1)]
        for val in nums:
          count[val] = count.get(val,0) + 1

        for val,freq in count.items():
            bucket[freq].append(val)

        """
        1:1, [ ]  [1,2]  [] [] [ ] [ ] [ ]
        2:1,  0    1    2   3   4   5   6  
    
        """
        res = []

        for freq in range(len(bucket)-1, -1 , -1):
            if bucket[freq]:
               for i in bucket[freq]:
                  res.append(i)
                  if len(res) == k:
                    return res
        



        
           
           
       