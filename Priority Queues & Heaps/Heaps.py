class MaxHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parent(self,index):
        if index/2 >= 0 and index/2 < self.size:
            return self.heapList[index/2]
        else:
            raise Exception("Invalid index.")

    def left_child(self,index):
        if index*2+1 < self.size and index*2+1 >= 0:
            return self.heapList[index*2+1]
        else:
            raise Exception("Invalid index.")

    def right_child(self,index):
        if index*2+2 < self.size and index*2+2 >= 0:
            return self.heapList[index*2+2]
        else:
            raise Exception("Invalid index.")

    def get_maximum(self):
        if self.size == 0:
            raise Exception("Heap is empty.")
        return self.heapList[0]

    def min_child(self,i):
        if i*2+1>=self.size:
            raise i*2
        else:
            if self.heapList[i*2+2] < self.heapList[i*2+1]:
                return i*2+2
            else:
                return i*2+1

    def max_child(self,i):
        if i*2 + 1>=self.size:
            return i*2
        else:
            if self.heapList[i*2+2] > self.heapList[i*2+1]:
                return i*2+2
            else:
                return i*2+1


    def percolate_down(self,i):
        if (i*2)<0 or not (i*2)<self.size:
            raise Exception("Index invalid.")
        while(i*2)<self.size:
            maximum_child = self.max_child(i)
            if self.heapList[i] < self.heapList[maximum_child]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[maximum_child ]
                self.heapList[maximum_child] = tmp
            i = maximum_child

    def percolate_up(self,i):
        if i//2 < 0 or not (i//2)< self.size:
            raise Exception("Index invalid.")
        while(i//2)>=0:
            if self.heapList[i//2] < self.heapList[i]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def delete_max(self):
        val = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.size -=1
        self.heapList.pop(0)
        self.percolate_down(0)
        return val

    def insert(self,val):
        self.heapList.append(val)
        self.percolate_up(self.size)
        self.size+=1



    def percolate_down_2(self,A,first,last):
        largest = 2*first+1
        while largest <= last:
            if largest < last and A[largest] > A[largest+1]:
                largest+=1
            if A[largest] > A[first]:
                self.swap(A,largest,first)
                first = largest
                largest = 2*first+1
            else:
                return
    def swap(self,A,x,y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp

class MinHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parent(self,index):
        if index/2 >= 0 and index/2 < self.size:
            return self.heapList[index/2]
        else:
            raise Exception("Invalid index.")

    def left_child(self,index):
        if index*2+1 < self.size and index*2+1 >= 0:
            return self.heapList[index*2+1]
        else:
            raise Exception("Invalid index.")

    def right_child(self,index):
        if index*2+2 < self.size and index*2+2 >= 0:
            return self.heapList[index*2+2]
        else:
            raise Exception("Invalid index.")

    def get_minimum(self):
        if self.size == 0:
            raise Exception("Heap is empty.")
        return self.heapList[0]

    def min_child(self,i):
        if i*2+1>=self.size:
            raise i*2
        else:
            if self.heapList[i*2+2] < self.heapList[i*2+1]:
                return i*2+2
            else:
                return i*2+1

    def max_child(self,i):
        if i*2 + 1>=self.size:
            return i*2
        else:
            if self.heapList[i*2+2] > self.heapList[i*2+1]:
                return i*2+2
            else:
                return i*2+1


    def percolate_down(self,i):
        if (i*2)<0 or not (i*2)<self.size:
            raise Exception("Index invalid.")
        while(i*2)<self.size:
            minimum_child = self.min_child(i)
            if self.heapList[i] > self.heapList[minimum_child]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minimum_child]
                self.heapList[minimum_child] = tmp
            i = minimum_child

    def percolate_up(self,i):
        if i//2 < 0 or not (i//2)< self.size:
            raise Exception("Index invalid.")
        while(i//2)>=0:
            if self.heapList[i//2] > self.heapList[i]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def delete_min(self):
        val = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.size -=1
        self.heapList.pop(0)
        self.percolate_down(0)
        return val

    def insert(self,val):
        self.heapList.append(val)
        self.percolate_up(self.size)
        self.size+=1


