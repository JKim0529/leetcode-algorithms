# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def solve(root,ans):
            if root==None:
                return
            ans.append(root.val)
            solve(root.left,ans)
            solve(root.right,ans)
        
        solve(root,ans)
        return ans