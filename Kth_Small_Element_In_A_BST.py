# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        ksmall = -9999999999 # store the Kth smallest  
        curr = root # to store the current node  

        while curr != None: 

            # Like Morris traversal if current does 
            # not have left child rather than  
            # printing as we did in inorder, we  
            # will just increment the count as the  
            # number will be in an increasing order  
            if curr.left == None: 
                count += 1

                # if count is equal to K then we  
                # found the kth smallest, so store  
                # it in ksmall  
                if count == k:  
                    ksmall = curr.val  

                # go to current's right child  
                curr = curr.right 
            else: 

                # we create links to Inorder Successor  
                # and count using these links  
                pre = curr.left  
                while (pre.right != None and 
                       pre.right != curr):  
                    pre = pre.right  

                # building links  
                if pre.right == None: 

                    # link made to Inorder Successor  
                    pre.right = curr  
                    curr = curr.left 

                # While breaking the links in so made  
                # temporary threaded tree we will check  
                # for the K smallest condition  
                else: 

                    # Revert the changes made in if part  
                    # (break link from the Inorder Successor)  
                    pre.right = None

                    count += 1

                    # If count is equal to K then we  
                    # found the kth smallest and so  
                    # store it in ksmall  
                    if count == k: 
                        ksmall = curr.val  

                    curr = curr.right 
        return ksmall # return the found value
