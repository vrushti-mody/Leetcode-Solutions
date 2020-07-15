# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge=defaultdict(list)
        for p in prerequisites:
            edge[p[0]].append(p[1]) # from:to 

        for k in range(numCourses): # for each start point
            stack=[k]
            visit=set()
            while stack:
                node=stack.pop(0)
                if visit and node==k:     # ignore the first start node
                    return False
                if node not in visit:
                    visit.add(node)
                    stack+=edge[node]
        return True
