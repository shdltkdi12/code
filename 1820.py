class Solution:
    def maximumInvitations(self, grid: list[list[int]]) -> int:
        girl_dic = defaultdict(lambda:-1)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            new = []
            for j in range(n):
                if grid[i][j] == 1:
                    new.append(j)
            grid[i] = new
        # print(grid)
        
        count = 0

        def f(boy):
            idx = indexes[boy]
            for girl in range(idx, n):
                if girl_dic[girl] < 0:
                    girl_dic[girl] = boy
                    indexes[boy] +=1
                    return True
                else:
                    return f(girl_dic[girl])
            return False

        for boy in range(m):
            if f(boy):
                count +=1
        return count      

