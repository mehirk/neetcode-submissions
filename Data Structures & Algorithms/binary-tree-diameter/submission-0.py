# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def get_depth(node):
            nonlocal max_diameter

            if not node:
                return 0
            
            left = get_depth(node.left)
            right = get_depth(node.right)

            current_diameter = left + right

            max_diameter = max(current_diameter, max_diameter)

            return 1 + max(left, right)
        get_depth(root)
        return max_diameter