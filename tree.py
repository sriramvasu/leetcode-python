import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def buildTree(nodes: list) -> TreeNode:
    n = len(nodes)
    if n == 0:
        return None
    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root
    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)   
            curParent = parentStack.popleft()
    return root