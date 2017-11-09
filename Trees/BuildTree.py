class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def build_tree(self,preorder,inorder):
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1:1+rootPos,inorder[:rootPos]])
        root.right = self.build_tree(preorder[rootPos+1:],inorder[rootPos+1:])
        return root