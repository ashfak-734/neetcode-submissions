class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1

        freq = [[] for _ in range(len(nums)+1)]

        for key,value in count.items():
            freq[value].append(key)

        res = []

        for val in reversed(freq):
            if val:
                for i in val:
                   if len(res) < k:
                      res.append(i)

        return res 

        