# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class StackElem(object):
    def __init__(self, x, l_limit, r_limit):
        self.val = x
        self.l_limit = l_limit
        self.r_limit = r_limit


class Solution(object):

    def find_new_root(self, branch, preorder):
        # Find first time an element in branch appears in preorder
        for c in preorder:
            if branch.find(c) is not -1:
                return c

        return -1


        return newroot

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Attempt at iterative solution:

        root_stack = []
        if len(preorder) == 0:
            return None
        # Append the first element
        elem = StackElem(preorder[0], 0, len(preorder))
        root_stack.append(elem)
        while len(root_stack) > 0:
            curr_root = root_stack.pop()
            inorder_index = inorder.index(curr_root.val)
            
            # do left:
            find_new_root(inorder[curr_root.left:inorder_index], preorder)
            # do right:
            find_new_root(inorder[inorder_index:curr_root.right], preorder)

            

