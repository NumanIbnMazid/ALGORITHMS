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
