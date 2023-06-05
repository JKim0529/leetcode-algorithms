class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return [""]
        elif not root.left and not root.right:
            return [str(root.val)]

        self.ret = []

        def helper(root, strr):
            if not root.left and not root.right:
                self.ret.append(strr + str(root.val))
                return
            
            if root.left:
                helper(root.left, strr + str(root.val)+"->")
            if root.right:
                helper(root.right, strr+ str(root.val)+"->")

        helper(root, "")

        return self.ret