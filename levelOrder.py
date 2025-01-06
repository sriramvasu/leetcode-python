from collections import deque
from typing import List, Optional
from tree import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        answer = []
        queue.appendleft([root, 0])
        if root==None:
            return []
        while(len(queue)>0):
            node, lvl = queue.pop()
            if node==None:
                continue
            if(len(answer)<lvl+1):
                answer.append([])
            answer[lvl].append(node.val)
            queue.appendleft([node.left, lvl+1])
            queue.appendleft([node.right, lvl+1])
        return answer