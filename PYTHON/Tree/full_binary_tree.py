"""
Notes: 
    - Every parent node/internal node has either two or no children.
    - Also known as a proper binary tree.
Full Binary Tree Theorems:
    i = the number of internal nodes
    n = the number of total nodes
    l = the number of leaves
    λ = the number of levels
    
    * The number of leaves:
        -> i + 1
    * The total number of nodes:
        -> 2i + 1
    * The number of internal nodes:
        -> (n - 1) / 2
    * The number of leaves:
        -> (n + 1) / 2
    * The total number of nodes:
        -> 2l - 1
    * The number of internal nodes:
        -> l - 1
    * The number of leaves at most:
        -> 2^λ - 1
"""