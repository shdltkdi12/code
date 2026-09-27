import sys
from collections import defaultdict

class A:
    def __init__(self):
        self.dic = {}
        self.reverse_dic = defaultdict(set)

def __main__():
    a = A()
    ans = []
    while True:
        cmd = input()
        chars = cmd.split(' ')
        if chars[0] == 'SET':
            _, key, val = chars
            if key in a.dic:
                prev = a.dic[key]
                a.reverse_dic[prev].remove(key)
            a.dic[key] = val
            a.reverse_dic[val].add(key)
            print(a.dic, a.reverse_dic)
        elif chars[0] == 'GET':
            key = chars[1]
            if key not in a.dic:
                ans.append('NULL')
            else:
                ans.append(str(a.dic[key]))
        elif chars[0] == 'UNSET':
            key = chars[1]
            if key in a.dic:
                prev = a.dic[key]
                a.reverse_dic[prev].remove(key)
                a.dic.pop(key)
        elif chars[0] == 'NUMWITHVALUE':
            val= chars[1]
            ans.append(str(len(a.reverse_dic[val])))
        elif chars[0] == 'END':
            print('\n'.join(ans))
            break

if __name__ == "__main__":
    __main__()

