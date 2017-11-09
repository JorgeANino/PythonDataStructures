from DinamicArrayQueue import DinamicArrayQueue
from DinamicArrayStack import DinamicArrayStack
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def setData(self,data):
        self.data = data

    def setRight(self,node):
        self.right = node

    def setLeft(self,node):
        self.left = node

    def getData(self):
        return self.data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.__ptr = 0

    def sumAll(self):
        if self.root == None:
            raise Exception("Tree is empty.")
        node = self.root
        q = DinamicArrayQueue()
        q.enqueue(node)
        sum = 0
        aux = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            sum+=aux.data
            if aux.left is not None:
                q.enqueue(aux.left)
            if aux.right is not None:
                q.enqueue(aux.right)
        return sum

    def setRoot(self,node):
        self.root = node

    def getRoot(self):
        return self.root

    def resetPtr(self):
        self.__ptr = 0

    def addNode(self,node,data):
        if node==None:
            self.root = Node(data)
        else:
            if data<=node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    self.addNode(node.left,data)
            else:
                if node.right == None:
                    node.right = Node(data)
                else:
                    self.addNode(node.right,data)

    def find_lca(self,node,a,b):
        if node == None:
            return node
        while node:
            if (a<= node.data and b> node.data) and (a> node.data and b>= node.data):
                return node
            if a<node.data:
                node = node.left
            else:
                node = node.right

    def printInOrder(self,node):
        if node == None:
            return
        if node.getLeft() is not None:
            self.printInOrder(node.getLeft())
        print(str(node.getData()))
        if node.getRight() is not None:
            self.printInOrder(node.getRight())


    def printPreOrder(self,node):
        if node == None:
            return
        print(str(node.getData()))
        if node.getLeft() is not None:
            self.printInOrder(node.getLeft())
        if node.getRight() is not None:
            self.printInOrder(node.getRight())

    def printPostOrder(self,node):
        if node == None:
            return
        if node.getLeft() is not None:
            self.printInOrder(node.getLeft())
        if node.getRight() is not None:
            self.printInOrder(node.getRight())
        print(str(node.getData()))


    def getSize_recursive(self,node):
        if node == None:
            return 0
        else:
            return self.getSize_recursive(node.left) + self.getSize_recursive(node.right) + 1

    def getSize_iterative(self,node):
        if node == None:
            return 0
        q = DinamicArrayQueue()
        q.enqueue(node)
        aux = None
        size = 0
        while not q.isEmptyQueue():
            aux = q.dequeue()
            size+=1
            if aux.left is not None:
                q.enqueue(aux.left)
            if aux.right is not None:
                q.enqueue(aux.right)
        return size

    def find_recursive(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        return self.find_recursive(node.left, data) or self.find_recursive(node.right, data)

    def find_bst_rec(self,data):
        curr = self.root
        if curr == None:
            raise Exception("Tree is empty.")
        while curr != None and curr.data != data:
            if data <= curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def find_bst_itr(self,data):
        curr = self.root
        if curr == None:
            raise Exception("Tree is empty")
        while curr != None:
            if data == curr.data:
                return curr
            if data <= curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def find_bst_min(self):
        curr = self.root
        if curr == None:
            raise Exception("Tree is empty.")
        while curr.left != None:
            curr = curr.left
        return curr

    def find_bst_max(self):
        curr = self.root
        if curr == None:
            raise Exception("Tree is empty.")
        while curr.right != None:
            curr = curr.right
        return curr

    def getInorderSuccesor(self,node):
        temp = None
        if node.right is not None:
            temp = node.right
            while temp.left is not None:
                temp = temp.left
        return temp

    def getInorderPredeccesor(self,node):
        temp = None
        if node.left is not None:
            temp = node.left
            while temp.right is not None:
                temp = temp.right
        return temp

    def levelTraversal_reversed(self,node):
        if node == None:
            return
        q = DinamicArrayQueue()
        s = DinamicArrayStack()
        aux = None
        q.enqueue(node)
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux.left is not None:
                q.enqueue(aux.left)
            if aux.right is not None:
                q.enqueue(aux.right)
            s.push(aux)
        while not s.isEmptyStack():
            aux = s.pop()
            if aux is not None:
                print(str(aux.data))

    def levelTraversal(self,root, result):
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
        return result

    def deleteBinaryTree(self,node):
        if node is None:
            return
        self.deleteBinaryTree(node.left)
        self.deleteBinaryTree(node.right)
        del node

    def clearBinaryTree(self):
        self.root = None

    def maxDepth_recursive(self,node):
        if node is None:
            return
        return max(self.maxDepth(node.left),self.maxDepth(node.right))+1

    def maxDepth_iterative(self):
        if self.root == None:
            return 0
        node = self.root
        q = []
        q.append([node,1])
        temp = 0
        while len(q)!=0:
            node,depth = q.pop()
            depth = max(temp,depth)
            if node.getLeft() is not None:
                q.append([node.getLeft(),depth+1])
            if node.getRight() is not None:
                q.append([node.getRight(),depth+1])
        return depth

    def deepest_node(self):
        if self.root == None:
            raise Exception("Tree is empty.")
        node = self.root
        q = DinamicArrayQueue()
        q.enqueue(node)
        aux = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux.left is not None:
                q.enqueue(aux.left)
            if aux.right is not None:
                q.enqueue(aux.right)
        return aux.data

    def delete_element(self,data):
        if self.root == None:
            raise Exception("Tree is empty.")
        q = DinamicArrayQueue()
        node = self.root
        q.enqueue(node)
        todelete = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux.data == data:
                todelete = aux
            if aux.left != None:
                q.enqueue(aux.left)
            if aux.right != None:
                q.enqueue(aux.right)
        if todelete != None:
            todelete.data = aux.data
            del aux

    def num_of_leaves(self):
        if self.root == None:
            raise Exception("Tree is empty")
        q = DinamicArrayQueue()
        node = self.root
        q.enqueue(node)
        cnt = 0
        aux = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux.left == None and aux.right == None:
                cnt += 1
            if aux.left != None:
                q.enqueue(aux.left)
            if aux.right != None:
                q.enqueue(aux.right)
        return cnt

    def num_of_fullnodes(self):
        if self.root == None:
            raise Exception("Tree is empty")
        q = DinamicArrayQueue()
        node = self.root
        q.enqueue(node)
        cnt = 0
        aux = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux.left != None and aux.right != None:
                cnt += 1
            if aux.left != None:
                q.enqueue(aux.left)
            if aux.right != None:
                q.enqueue(aux.right)
        return cnt

    def num_of_halfnodes(self):
        if self.root == None:
            raise Exception("Tree is empty")
        q = DinamicArrayQueue()
        node = self.root
        q.enqueue(node)
        cnt = 0
        aux = None
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if (aux.left != None and aux.right == None) or (aux.left == None and aux.right != None):
                cnt += 1
            if aux.left != None:
                q.enqueue(aux.left)
            if aux.right != None:
                q.enqueue(aux.right)
        return cnt


    def isIdenticalTree(self,node1,node2):
        if  node1== None and node2 == None:
            return True
        if  (not node1.left and not node2.left) and (not node1.right and node2.right) and (node1.data == node2.data):
            return True
        if (node1.data != node2.data) or (node1.left and not node2.left) or(node2.left and not node1.left) or\
            (node1.right and not node2.right) or (not node1.right and node2.right):
            return False
        left = self.isIdenticalTree(node1.left,node2.left)
        right = self.isIdenticalTree(node1.right,node2.right)
        return left and right

    def diameter(self,node):
        if not node:
            return 0
        left = self.diameter(node.left)
        right = self.diameter(node.right)
        if left+right > self.__ptr:
            ptr = left+right
        return max(left,right)+1

    def findMaxSumLevel(self):
        if self.root == None:
            raise Exception("Tree is empty.")
        node = self.root
        q = DinamicArrayQueue()
        q.enqueue(node)
        q.enqueue(None)
        aux = None
        level = maxlevel = currsum = maxsum = 0
        while not q.isEmptyQueue():
            aux = q.dequeue()
            if aux == None:
                if currsum > maxsum:
                    maxsum = currsum
                    maxlevel = level
                currsum = 0
                if not q.isEmptyQueue():
                    q.enqueue(None)
                    level +=1
            else:
                currsum += aux.data
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)

    def paths_finder(self,node):
        def paths_appender(node,path,paths):
            if not node:
                return 0
            path.append(node.data)
            paths.append(path)
            paths_appender(node.left,path+[node.data],paths)
            paths_appender(node.right,path+[node.data],paths)
        paths = []
        paths_appender(node,[],paths)
        print("Paths: ",paths)

    def sumNumbers(self,node):
        def cal_sum(node,current,sum):
            if not node:
                return
            current=current*10+node.data
            if not node.left and not node.right:
                sum[0]+=current
                return
            cal_sum(node.left,current,sum)
            cal_sum(node.right,current,sum)
        if not node:
            return 0
        current = 0
        sum = [0]
        cal_sum(node,current,sum)
        return sum[0]

    def mirrorTree(self,node):
        if node != None:
            self.mirrorTree(node.left)
            self.mirrorTree(node.right)
            temp = node.left
            node.left= node.right
            node.right = temp
        return node

    def isMirrorTree(self,node1,node2):
        if node1 == None and node2 == None:
            return True
        if node1 ==None or node2 == None:
            return False
        if node1.data != node2.data:
            return False
        else:
            return self.isMirrorTree(node1.left,node2.right) and self.isMirrorTree(node1.right,node2.left)

    def lca(self,node,alpha,beta):
        if not node:
            return None
        if node.data == alpha or node.data == beta:
            return node
        left = self.lca(node.left,alpha,beta)
        right = self.lca(node.right,alpha,beta)
        if left and right:
            return node
        else:
            return left if left else right

    def print_ancestors(self,root,node):
        if root == None:
            return False
        if root.left == node or root.right == node or self.print_ancestors(root.left,node) or self.print_ancestors(root.right,node):
            print(node.data)
            return True
        return False

    def zigZagTraversal(self):
        result = []
        currentLvl = []
        aux = self.root
        if self.root == None:
            raise Exception("Tree is empty.")
        currentLvl.append(aux)
        leftToRight = True
        while len(currentLvl) > 0:
            levelresult = []
            nextLvl = []
            while len(currentLvl) > 0:
                node = currentLvl.pop()
                levelresult.append(node.data)
                if leftToRight:
                    if node.left != None:
                        nextLvl.append(node.left)
                    if node.right != None:
                        nextLvl.append(node.right)
                else:
                    if node.right != None:
                        nextLvl.append(node.right)
                    if node.left!=None:
                        nextLvl.append(node.left)
            currentLvl= nextLvl
            result.append(levelresult)
            leftToRight = not leftToRight
        return result


    def buildTreePreOrder(self,string,i):
        new_node = Node(string[i])
        new_node.left = new_node.right = None
        if string[i] == "L":
            return new_node
        i+=1
        new_node.left = self.buildTreePreOrder(string,i)
        i+=1
        new_node.right = self.buildTreePreOrder(string,i)
        return new_node

    def isBST(self,node):
        if node == None:
            return True
        if node.left.data <= node.data and node.right.data > node.data:
            return True and self.isBST(node.left) and self.isBST(node.right)
        else:
            return False


p = BinarySearchTree()
p.addNode(p.root,5)
p.addNode(p.root,10)
p.addNode(p.root,7)
p.addNode(p.root,4)
r = []
p.printInOrder(p.root)
print("-----")
p.printPreOrder(p.root)
print("-----")
p.printPostOrder(p.root)
print("-----")
print(str(p.getSize_recursive(p.root)))
print("-----")
r = p.levelTraversal(p.root,r)
print(r)
print("-----")
print(p.levelTraversal_reversed(p.root))



