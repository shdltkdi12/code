from functools import cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        time = 0
        directions = [[-2,1],[-2,-1],[2,1],[2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        queue = deque([(0,0)])
        visited = set()
        while queue:
            # print(queue)
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                old_dis_i = abs(x-i)
                old_dis_j = abs(y-j)

                for direction in directions:
                    ith= direction[0] + i
                    jth = direction[1] + j
                    new_dis_i = abs(x-ith)
                    new_dis_j = abs(y-jth)

                    if old_dis_i > new_dis_i or old_dis_j > new_dis_j:
                        
                        queue.append([ith, jth])
                

            if queue:
                time+=1


        return time
            
