class Node:
    def __init__(self,parent,data=None):
        self.parent = parent
        self.data = data
        self.childList = []
        if parent is None:
           self.birthOrder = 0
        else:
            self.birthOrder = len(parent.childList)
            parent.childList.append(self)

    def nChildren(self):
        return len(self.childList)

    def nthChild(self,n):
        return self.childList[n]

    def fullPath(self):
        result = []
        parent = self.parent
        kid = self
        while parent:
            result.insert(0,kid.birthOrder)
            parent,kid = parent.parent,parent
        return result


class NodeId:
    def __init__(self,path):
        self.path = path

    def __str__(self):
        L = map(str,self.path)
        return "".join(L,"/")

    def find(self,node):
        return self.__reFind(node,0)

    def __reFind(self,node,i):
        if i>=len(self.path):
            return node.data
        else:
            childNo = self.path[i]
        try:
            child = node.nthChild(childNo)
        except IndexError:
            return None
        return self.__reFind(child,i+1)

