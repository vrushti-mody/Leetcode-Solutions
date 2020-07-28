# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

class Solution(object):
    
    def __init__(self):
        self.path = []
        self.paths = []
        
    def allPathsSourceTarget(self, graph):
        self.dfs(0, len(graph)-1, graph)
        return self.paths
    
    def dfs(self, index, destination, graph):
        self.path.append(index)
        nodes = graph[index]
        if nodes:
            for node in nodes:
                if(node == destination):
                    self.path.append(node)
                    self.paths.append(list(self.path))
                    self.path.pop(-1)
                else:
                    self.dfs(node, destination, graph)
                    self.path.pop(-1)
      
