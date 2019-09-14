# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None;

        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        preorder.remove(root.val)

        left_sub_inorder = inorder[0:index:]
        root.left = self.buildTree(preorder, left_sub_inorder)

        right_sub_inorder = inorder[index+1::]
        root.right = self.buildTree(preorder, right_sub_inorder)

        return root
