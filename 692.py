from sortedcontainers import SortedList, SortedDict
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = SortedDict(lambda x:-x)
        counter = Counter(words)
        for key, val in counter.items():
            if val not in dic:
                dic[val] = SortedList([key])
            else:
                dic[val].add(key)
        keys = list(dic.keys())
        ans = []
        i = 0
        while k > 0:
            # print(i,k, len(keys), keys[i])
            if len(dic[keys[i]]) > k:
                ans += list(dic[keys[i]][:k])
            else:
                ans += list(dic[keys[i]])
            k -= len(dic[keys[i]])
            i+=1
        return ans

