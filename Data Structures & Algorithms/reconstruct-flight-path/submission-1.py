class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = collections.defaultdict(list)

        for a, b in tickets:
            adj[a].append(b)

        res = []

        def dfs(src):
            while adj[src]:
                v = adj[src].pop()
                dfs(v)

            res.append(src)

        dfs("JFK")

        return res[::-1]