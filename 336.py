ass Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []

        dic = {}
        n= len(words)
        for i in range(n):
            dic[words[i]] = i
        

        def is_palindrome(str):
            i = 0
            j = len(str)-1
            while i < j:
                if str[i] != str[j]:
                    return False
                i+=1
                j-=1
            return True

        if '' in dic:
            for i in range(n):
                if words[i] !='' and is_palindrome(words[i]):
                    ans.append([i, dic['']])


        for i in range(n):
            word = words[i]
            ni = len(word)
            for j in range(ni):
                # split
                prefix = word[0:j+1]
                suffix = word[j+1:ni]
                is_prefix = is_palindrome(prefix)
                is_suffix = is_palindrome(suffix)
                # if prefix is palindrome and suffix is not
                if is_prefix and not is_suffix:
                    reverse = ''.join(reversed(suffix))
                    if reverse in dic and dic[reverse] != i:
                        ans.append([dic[reverse], i])
                # if suffix is palindrome and prefix is not
                if is_suffix and not is_prefix:
                    reverse = ''.join(reversed(prefix))
                    if reverse in dic and dic[reverse] != i:
                        ans.append([i, dic[reverse]])
                # if both?
                if is_prefix and is_suffix:
                    reverse_pre = ''.join(reversed(prefix))
                    reverse_suf = ''.join(reversed(suffix))
                    if reverse_pre in dic and dic[reverse_pre] != i:
                        ans.append([i, dic[reverse_pre]])
                    if reverse_suf in dic and dic[reverse_suf] != i:
                        ans.append([dic[reverse_suf], i])
                
        return ans
