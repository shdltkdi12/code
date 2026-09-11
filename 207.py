from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(numCourses):
            graph[i]

        for vertex, edge in prerequisites:
            graph[vertex].append(edge)
        
        def f(node):
            if node in visiting:
                return True
            if node in visited:
                return False

            visiting.add(node)
            for edge in graph[node]:
                if f(edge):
                    # print(node, edge)
                    return True
            visiting.remove(node)
            visited.add(node)
            return False
        visited = set()
        for vertex in graph:
            if vertex in visited:
                continue

            visiting = set()
            if f(vertex):
                return False
        return True
