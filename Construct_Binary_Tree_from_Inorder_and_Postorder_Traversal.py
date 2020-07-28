# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note: You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
       
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        i, j = len(inorder) - 1, len(postorder) - 1
        stack = []
        root = TreeNode(postorder[i])
        i -= 1
        stack.append(root)
        
        while i >= 0:
            curr = TreeNode(postorder[i])
            i -= 1
            prev = None
            
            while stack and stack[-1].val == inorder[j]:
                prev = stack.pop()
                j -= 1
            
            if prev:
                prev.left = curr
            else:
                stack[-1].right = curr
            
            stack.append(curr)
        
        return root
        
