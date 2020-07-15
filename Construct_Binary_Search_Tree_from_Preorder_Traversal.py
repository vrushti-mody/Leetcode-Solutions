# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
         
  
        # The first element of pre[] is always root 
        root = TreeNode(preorder[0]) 
  
        s = [] 
  
        # append root 
        s.append(root) 
  
        i = 1
  
        # Iterate through rest of the size-1 
        # items of given preorder array 
        while ( i < len(preorder)):  
            temp = None
  
            # Keep on popping while the next value  
            # is greater than stack's top value.  
            while (len(s) > 0 and preorder[i] > s[-1].val):  
                temp = s.pop() 
              
            # Make this greater value as the right child 
            # and append it to the stack 
            if (temp != None):  
                temp.right = TreeNode(preorder[i]) 
                s.append(temp.right) 
              
            # If the next value is less than the stack's top 
            # value, make this value as the left child of the  
            # stack's top node. append the new node to stack 
            else : 
                temp = s[-1] 
                temp.left = TreeNode(preorder[i]) 
                s.append(temp.left) 
            i = i + 1
          
        return root 
      
