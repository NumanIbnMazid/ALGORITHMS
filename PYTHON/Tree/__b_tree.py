"""
Keywords: B-Tree, Self balancing Key
Notes:
    - Special Type of Self Balancing Search Tree.
    - Each node can have more than one key and can have more than two children.
    - Generalized form of Binary Search Tree.
    - Also known as Height-Balance m-way tree.
    - A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size.
    - Every node except root must contain at least t-1 keys. The root may contain minimum 1 key.
    - All nodes (including root) may contain at most 2*t – 1 keys.
    - Insertion of a Node in B-Tree happens only at Leaf Node.
B-Tree Property:
    - For each node x, the keys are stored in increasing order.
    - In each node, there is a boolean value x.leaf which is true if x is a leaf.
    - If n is the order of the tree, each internal node can contain at most n - 1 keys along with a pointer to each child.
    - Each node except root can have at most n children and at least n/2 children.
    - All leaves have the same depth (i.e. height-h of the tree).
    - The root has at least 2 children and contains a minimum of 1 key.
    - If n ≥ 1, then for any n-key B-tree of height h and minimum degree t ≥ 2, h ≥ logt (n+1)/2.
"""

