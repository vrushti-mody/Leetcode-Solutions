# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).


from queue import SimpleQueue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
       
        val_list = []
        q = SimpleQueue()
        q.put((root,0))

        while not q.empty():
            cur_node, pos = q.get()
            if cur_node:
                try:
                    val_list[pos].append(cur_node.val)
                except IndexError:
                    val_list.append([cur_node.val])
                q.put((cur_node.left,pos+1))
                q.put((cur_node.right, pos+1))

        return val_list[::-1]
