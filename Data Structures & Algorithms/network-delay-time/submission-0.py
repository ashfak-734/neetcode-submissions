import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)

        for u,v,time in times:
            g[u].append((v,time))

        min_times = {}
        minheap = [(0,k)]

        while minheap:
            k_to_i,i = heapq.heappop(minheap)

            if i in min_times:
                continue

            min_times[i] = k_to_i

            for nei,nei_time in g[i]:
                if nei in min_times:
                    continue
                
                heapq.heappush(minheap,(k_to_i + nei_time,nei))

        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1 





        