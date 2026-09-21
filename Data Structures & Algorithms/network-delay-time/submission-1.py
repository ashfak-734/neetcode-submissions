class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)

        for u,v,t in times:
            g[u].append((v,t))

        min_times = {}
        minheap = [(0,k)]

        while minheap:
            time,source = heapq.heappop(minheap)

            if source in min_times:
                continue

            min_times[source] = time

            for nei,nei_time in g[source]:
                if nei in min_times:
                    continue

                heapq.heappush(minheap,(time + nei_time,nei))

        if len(min_times) == n:
            return max(min_times.values())
        else:
            return  -1 

        