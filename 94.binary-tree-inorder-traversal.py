# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    # Iterative solution:
    def inorderTraversalIterative(self, root, localList):
        stack = []
        result = []
        node = 0
        while 1:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right

    
    # Recursive solution:   
    def inorderTraversalRecursive(self, root, localList):
        if root is None:
            return
        
        self.inorderTraversalRecursive(root.left, localList)
        localList.append(root.val)
        self.inorderTraversalRecursive(root.right, localList)
        
        return localList 
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        localList = []
        #return self.inorderTraversalRecursive(root, localList)
        return self.inorderTraversalIterative(root, localList) 
