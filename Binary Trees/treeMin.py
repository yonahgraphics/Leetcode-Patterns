class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


import math
# Recursion
# Time Complexity: O(n) since we process every node atmost once
# Space Complexity: O(n) since we make exactly n function calls
def treeMinRecursive(root):
    if root is None:
        return math.inf
    minLeft  = treeMinRecursive(root.left)
    minRight = treeMinRecursive(root.right)
    return min(root.val, minLeft, minRight)
    
# BFS Iterative
# Time Complexity: O(n) since we make exactly n function calls
# Space Complexity: O(1) since we have atmost 3 nodes (constant) on the queue
# Alvin says it's O(n)  
def treeMinIterativeBFS(root):
    if root is None:
        return math.inf
    minimum = math.inf
    queue = []
    queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        minimum = min(minimum, curr.val)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return minimum

# DFS Iterative
# Time Complexity: O(n) since we make exactly n function calls
# Space Complexity: O(3)=== O(1) since we have atmost 3 function calls on the stack
# Alvin says it's O(n)
def treeMinIterativeDFS(root):
    if root is None:
        return math.inf
    minimum = math.inf
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        minimum = min(minimum, curr.val)
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return minimum
    


   
if __name__ == "__main__":
    #      1
    #     / \
    #    2   3
    #   /\    \
    #  4  5    6

    A = Node(1)
    B = Node(2)
    C = Node(3)
    E = Node(4)
    F = Node(-5)
    G = Node(6)

    A.left  = B
    A.right = C
    B.left  = E
    B.right = F
    C.right = G

    print(treeMinRecursive(A))
    print(treeMinIterativeBFS(A))
    print(treeMinIterativeDFS(A))

