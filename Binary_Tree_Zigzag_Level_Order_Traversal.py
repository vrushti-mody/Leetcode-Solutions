# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        q = [root]
        leftToRight = False
        
        while q:
            count = len(q)
            temp = []
            while count > 0:
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                count -= 1
                
            if leftToRight:
                result.append(temp[::-1])
                leftToRight = False
            else:
                result.append(temp)
                leftToRight = True
        return result
