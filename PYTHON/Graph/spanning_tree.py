"""
Notes:
    - Sub-graph of an undirected connected graph.
    - Includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed then it will not be a spanning tree.
    - The edges may or may not have weights assigned to them.
    - The total number of spanning trees with n vertices that can be created from a complete graph is equal to n^(n-2).
    - If we have n = 4, the maximum number of possible spanning trees is equal to 4^4-2 = 16. Thus, 16 spanning trees can be formed from a complete graph with 4 vertices.
"""