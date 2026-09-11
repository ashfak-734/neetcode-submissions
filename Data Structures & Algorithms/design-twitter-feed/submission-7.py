import heapq
class Twitter:

    def __init__(self):
        self.tweet_map = {}
        self.follow_map = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []

        self.tweet_map[userId].append((self.count,tweetId))
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        if userId not in self.follow_map:
            self.follow_map[userId] = set()

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId])-1
                count,tweet = self.tweet_map[followeeId][index]
                minheap.append([count,tweet,index-1,followeeId])

        heapq.heapify(minheap)

        while minheap and len(res)<10:
            count,tweet,index,followeeId = heapq.heappop(minheap)
            res.append(tweet)
            if index >= 0:
                count,tweet = self.tweet_map[followeeId][index]
                heapq.heappush(minheap,[count,tweet,index-1,followeeId])
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
              self.follow_map[followerId] = set()
        
        self.follow_map[followerId].add(followeeId)
      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.follow_map:
                self.follow_map[followerId].discard(followeeId)

   

        
