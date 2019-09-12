import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverseArray(root, i, tree):
            if root is None:
                tree[i] = None
                return
            
            traverseArray(root.left, 2*i, tree)
            traverseArray(root.right, 2*i+1, tree)
        # First step, we want to create a level-order search array (O(log(n)))
        tree = [-1]*10000000
        traverseArray(root, 1, tree)
        
        # Shift to the left because we start at index 1
        tree = tree[1:]
        
        # Second we parse the array for leaf nodes to find the min (O(n))

        for i in range(len(tree)):
        # Find the leaf nodes
            
            if tree[2*i] is None and tree[2*i+1] is None:
                if i == 0:
                    result = 1
                    break
                    
                result = math.floor(math.log2(i) + 1)
                break
            
        return result
                    
