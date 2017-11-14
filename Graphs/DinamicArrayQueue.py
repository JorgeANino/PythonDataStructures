class DinamicArrayQueue:
    def __init__(self,maxSize=None):
        self.maxSize = maxSize
        self.queue = []
        self.length = 0

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return self.length

    def __del__(self):
        self.clear()

    def clear(self):
        self.queue = []
        self.length = 0

    def enqueue(self,data):
        if self.length == self.maxSize:
            raise Exception("FullQueueException.")
        self.queue.append(data)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception("EmptyQueueException.")
        temp = self.queue[0]
        self.queue.remove(self.queue[0])
        self.length -=1
        return temp

    def front(self):
        return self.queue[0]

    def queueSize(self):
        return self.length

    def isEmptyQueue(self):
        return self.length == 0

    def isFullQueue(self):
        return self.length == self.maxSize