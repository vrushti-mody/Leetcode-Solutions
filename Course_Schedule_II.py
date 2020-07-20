# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degree,adj=self.create_adj(numCourses,prerequisites)
        visited = [0 for i in range(numCourses)]
        stack = []
        for i in range(numCourses):
            if not visited[i] and not self.dfs(i,visited,stack,adj):
                return []
        return stack[::-1]
    def create_adj(self,n,graph):
        adj = {}
        in_degree= [0 for i in range(n)]
        for i in graph:
            in_degree[i[0]]+=1
            if i[1] in adj:
                adj[i[1]].append(i[0])
            else:
                adj[i[1]] = [i[0]]
        return in_degree,adj
    def dfs(self, node, visited,stack,adj):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        if node in adj:
            for i in adj[node]:
                if not self.dfs(i,visited,stack,adj):
                    return False
        visited[node]=1
        stack.append(node)
        return True
