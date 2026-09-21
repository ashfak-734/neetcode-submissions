from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1 
        self.tweets[userId].append((self.time,tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        res = []
        
        self.following[userId].add(userId)
        for user in self.following[userId]:
            index = len(self.tweets[user]) - 1
            if index >= 0:
               time,tweetID = self.tweets[user][index]
               minheap.append([time,tweetID,index-1,user])

        heapq.heapify(minheap)

        while minheap and len(res)<10:
            _,tweeID,index,user = heapq.heappop(minheap)
            res.append(tweeID)
            if index >= 0:
                time,tweetID = self.tweets[user][index]
                heapq.heappush(minheap,[time,tweetID,index-1,user])

        return res 


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
