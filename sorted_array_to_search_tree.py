# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return
        ind=len(nums)//2            #Because the arr or list is shorted you should thake middle number as the root
        root=TreeNode(nums[ind])    #Now you can assign the left branch and perform recurtion with left remaining list
        root.left=self.sortedArrayToBST(nums[:ind])     #Same for the right remaining list
        root.right=self.sortedArrayToBST(nums[ind+1:])
        return root

        