# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)

            index = inorder_map[root_val]

            # Build right subtree first
            root.right = build(index + 1, right)
            root.left = build(left, index - 1)

            return root

        return build(0, len(inorder) - 1)