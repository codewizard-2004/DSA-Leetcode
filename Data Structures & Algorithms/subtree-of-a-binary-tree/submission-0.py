def compare(node1, node2):
    if not node1 and not node2:
        return True

    if not node1 or not node2:
        return False

    if node1.val != node2.val:
        return False

    return compare(node1.left, node2.left) and compare(node1.right, node2.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if root.val == subRoot.val and compare(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )