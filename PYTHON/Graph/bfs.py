"""
Keywords: Breadth first search, recursive algorithm
Notes:
    - Vertex Category:
        * Visited
        * Not Visited
"""

import collections


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        
        # if not visited then mark it as visited and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)


print("\n------- Implementation Two -------\n")

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queue = []
result = ""

def bfs(graph, node, visited):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0) # LIFO
        # print(m, end=" ")
        global result
        result += m + " -> "
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                

print("Following is the Breadth-First Search")
bfs(graph=graph, node="5", visited=visited)    # function calling
print(result)
