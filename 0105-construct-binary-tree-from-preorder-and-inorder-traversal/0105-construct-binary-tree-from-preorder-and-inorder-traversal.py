# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            index = inorder_map[root_val]

            root.left = build(left, index - 1)
            root.right = build(index + 1, right)

            return root

        return build(0, len(inorder) - 1)