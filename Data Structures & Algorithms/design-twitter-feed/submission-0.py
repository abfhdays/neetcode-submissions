import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.following = defaultdict(set)   # CHANGED: new users start with an empty set
        self.tweets = defaultdict(list)     # CHANGED: new users start with an empty list
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.count))  # CHANGED: store timestamp too
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        users = self.following[userId].union({userId})

        for uid in users:
            if self.tweets[uid]:
                ind = len(self.tweets[uid]) - 1          # CHANGED: last valid index
                tuid, count = self.tweets[uid][ind]      # CHANGED: read that tweet
                heapq.heappush(minheap, (-count, tuid, uid, ind))

        res = []
        while minheap and len(res) < 10:                 # CHANGED: limit results, not heap
            negcount, tuid, uid, ind = heapq.heappop(minheap)
            res.append(tuid)

            if ind > 0:                                 # CHANGED: an earlier tweet exists
                ind -= 1
                tuid, count = self.tweets[uid][ind]      # CHANGED: look it up by user
                heapq.heappush(minheap, (-count, tuid, uid, ind))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)