from DinamicArrayQueue import DinamicArrayQueue

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setLeftNode(self,node):
        self.left = node

    def getLeftNode(self):
        return self.left

    def setRightNode(self,node):
        self.right = node

    def getRightNode(self):
        return self.right

class BinaryTree:
    def __init__(self,root=None):
        self.root = root
        self.max = 0
        self.length = 0

    def getRoot(self):
        return self.root

    def insertRight(self,data):
        if not self.root:
            self.root = Node(data)
            return
        if not self.root.right:
            self.root.right = Node(data)
            return
        temp = Node(data)
        temp.right = self.root.right
        self.root.right = temp
        self.length += 1

    def insertLeft(self,data):
        if not self.root:
            self.root = Node(data)
            return
        if not self.root.left:
            self.root.left = Node(data)
            return
        temp = Node(data)
        temp.left = self.root.left
        self.root.left = temp
        self.length += 1

    def find_recursive(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        return self.find_recursive(node.left, data) or self.find_recursive(node.right, data)


    def preorder_recursive(self,node,result):
        if not node:
            return
        result.append(node)
        self.preorder_recursive(node.left,result)
        self.preorder_recursive(node.right,result)

    def preorder_iterative(self,root,result):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

    def inorder_recursive(self,root,result):
        if not root:
            return
        self.inorder_recursive(root.left,result)
        result.append(root)
        self.inorder_recursive(root.right,result)

    def inorder_iterative(self,root,result):
        if not root:
            return
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right

    def postorder_recursive(self,root,result):
        if not root:
            return
        self.postorder_recursive(root.left,result)
        self.postorder_recursive(root.right,result)
        result.append(root)

    def postorder_iterative(self,root,result):
        if not root:
            return
        visited = set()
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None

    def level_order(self,root, result):
        if root is None:
            return
        q = DinamicArrayQueue()
        q.enqueue(root)
        node = None
        while not q.isEmptyQueue():
            node = q.dequeue()
            result.append(node.data)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    def find_max_using_level_order(self,root):
        if root is None:
            return
        q = DinamicArrayQueue()
        q.enqueue(root)
        node = None
        max = 0
        while not q.isEmptyQueue():
            node = q.dequeue()
            if max < node.data:
                max = node.data
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return max



    max = float("-infinity")
    def getMax(self,node):
        aux = node
        global max
        if not aux:
            return max
        if aux.data > max:
           max = aux.data
        self.getMax(node.left)
        self.getMax(node.right)
        return max




    def find_iterative(self,root,data):
        if root is None:
            return False
        q = DinamicArrayQueue()
        q.enqueue(root)
        node = None
        while not q.isEmptyQueue():
            node = q.dequeue()
            if node.data == data:
                return True
            if node.left is not None:
               q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return False

    def getSize_recursive(self,node):
        if node == None:
            return
        else:
            return self.getSize_recursive(node.left) + self.getSize_recursive(node.right) + 1


n = BinaryTree()
n.insertLeft(5)
n.insertLeft(6)
n.insertLeft(7)
n.insertLeft(8)
print(n.root.left.data)
