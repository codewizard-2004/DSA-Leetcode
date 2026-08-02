# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootList = []
        subList = []
        
        def dfs(node, arr):  
            if not node:
                arr.append("#")
                return
            arr.append(str(node.val))
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        dfs(root, rootList)
        dfs(subRoot, subList)

        return "".join(subList) in "".join(rootList)


        