# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lvls = {}
        lvls[0] = [root.val]

        def dfs(node, lvl):
            if not node:
                return
            if lvl not in lvls:
                lvls[lvl] = [node.val]
            else:
                lvls[lvl].append(node.val)

            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

        dfs(root.left, 1)
        dfs(root.right, 1)

        return list(lvls.values())

        
        