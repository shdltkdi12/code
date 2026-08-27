class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dic = Counter(p)
        static = list(p_dic.keys())

        n = len(s)
        ans = []
        i = 0

        if len(p) == 1:
            for i in range(n):
                if s[i] == p:
                    ans.append(i)
            return ans

        count = len(p)
        while True:
            # print(i)
            while i < n and s[i] not in p_dic:
                i +=1
            if i == n:
                break
            p_dic[s[i]] -=1
            count -=1

            j= i+1
            while j < n:
                # invalid window, immediately hop over that
                if s[j] not in p_dic:
                    i = j+1
                    count = len(p)
                    p_dic = Counter(p)
                    break
                
                p_dic[s[j]] -=1
                # valid window, move i until u refresh the current key that is giving negative
                if p_dic[s[j]] < 0:
                    while i < j and p_dic[s[j]] < 0:
                        p_dic[s[i]] +=1
                        if s[i] != s[j]: count +=1 
                        i +=1
                else:
                    count -=1
                
                # check count so we can add the i index
                if count == 0:
                    ans.append(i)
                    count +=1
                    p_dic[s[i]] +=1
                    i +=1
                j+=1
            
            if j >= n or i >= n:
                break

        return ans
