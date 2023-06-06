# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], path="") -> List[str]:
        if path: path+="->"
        left = self.binaryTreePaths(root.left, path+str(root.val)) if root.left else []
        right = self.binaryTreePaths(root.right, path+str(root.val)) if root.right else []

        return left+right or [path+str(root.val)]