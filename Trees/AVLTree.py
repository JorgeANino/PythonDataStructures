class AVLNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.balanceFactor = 0
        self.left = left
        self.right = right


class AVLTree:

    def __init__(self,root=None):
        self.root = root

    def height(self):
        return self.rec_height(self.root)

    def rec_height(self,root):
        if root == None:
            return 0
        else:
            leftH = self.rec_height(root.left)
            rightH = self.rec_height(root.right)
            if leftH>rightH:
                return 1+leftH
            else:
                return 1+rightH


    def single_left_rotate(self,root):
        W = root.left
        root.left = W.right
        W.right = root
        return W

    def single_right_rotate(self,root):
        W = root.right
        root.right = W.left
        W.left = root
        return W

    def left_right_rotate(self,root):
        X = root.left
        if X.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor=0
            root=self.single_left_rotate(root)
        else:
            Y=X.right
            if Y.balanceFactor==-1:
                root.balanceFactor=1
                X.balanceFactor=0
            elif Y.balanceFactor==0:
                root.balanceFactor=0
                X.balanceFactor=0
            else:
                root.balanceFactor=0
                X.balanceFactor=-1
            Y.balanceFactor = 0
            root.left = self.single_right_rotate(X)
            root=self.single_left_rotate(root)
        return root

    def right_left_rotate(self,root):
        X = root.right
        if X.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.single_right_rotate(root)
        else:
            Y = X.left
            if Y.balanceFactor == -1:
                root.balanceFactor = 0
                X.balanceFactor = 1
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = -1
                X.balanceFactor = 0
            Y.balanceFactor = 0
            root.right = self.single_left_rotate(X)
            root = self.single_right_rotate(root)
        return root