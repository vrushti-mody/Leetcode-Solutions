# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.d = [[0,0]]
        def f(l,p,r):
            if r:
                if len(self.d)<=l:
                    self.d.append([p,p])
                else:
                    self.d[l]=[min(self.d[l][0],p),max(self.d[l][1],p)]
                f(l+1,2*p,r.left)
                f(l+1,2*p+1,r.right)
        f(0,0,root)
        return max(d[1] - d[0] + 1 for d in self.d )
        
