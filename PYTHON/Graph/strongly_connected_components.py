"""
Notes:
    - Portion of a directed graph in which there is a path from each vertex to another vertex.
    - It is applicable only on a directed graph.
    - These components can be found using `Kosaraju's Algorithm`.
    - `Kosaraju's Algorithm` is based on the depth-first search algorithm implemented twice.
"""

from collections import defaultdict

class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        
    # add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)
        
    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end="")
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex=visited_vertex)
    
    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(d=i, visited_vertex=visited_vertex, stack=stack)
        stack = stack.append(d)
        
    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(s=j, d=i)
        return g
    
    # print the strongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)
        
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(d=i, visited_vertex=visited_vertex, stack=stack)
                
        gr = self.transpose()
        
        visited_vertex = [False] * (self.V)
        
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex=visited_vertex)
                print("")
                
                
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
