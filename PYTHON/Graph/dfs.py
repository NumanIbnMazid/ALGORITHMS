"""
Keywords: Depth First Search, Depth first traversal, recursive algorithm
Notes:
    - Vertex Category:
        * Visited
        * Not Visited
"""


def dfs(graph, start, visited=None):
    if visited == None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph=graph, start=next, visited=visited)
    return visited


graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

dfs(graph=graph, start='0')


print("\n------- Implementation Two -------\n")

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

result = ""

def bfs(graph, node, visited=None):
    if node not in visited:
        # print(node)
        global result
        result += node + " -> "
        visited.add(node)
        
        for neighbour in graph[node]:
            bfs(graph=graph, node=neighbour, visited=visited)
            

print("Following is the Depth-First Search")
bfs(graph=graph, node="5", visited=visited)
print(result)
