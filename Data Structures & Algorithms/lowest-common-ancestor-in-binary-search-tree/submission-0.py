# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                #LCA is in left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # LCA is in right subtree
                root = root.right
            else:
                # LCA is at the node which splits p and q into seperate brances
                return root
        