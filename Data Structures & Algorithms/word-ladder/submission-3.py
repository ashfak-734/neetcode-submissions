
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = collections.defaultdict(list)

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        q = collections.deque()

        q.append(beginWord)
        res = 1

        seen = set()
        seen.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in seen:
                            seen.add(neiword)
                            q.append(neiword)        

            res+=1

        return 0

              
        

        
       






        