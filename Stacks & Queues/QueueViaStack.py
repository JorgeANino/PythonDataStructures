from DinamicArrayStack import DinamicArrayStack
class QueueViaStack:

    def __init__(self):
        self.queue = DinamicArrayStack()
        self.stack = DinamicArrayStack()

    def __len__(self):
        return str(self.stack)


    def enqueue(self,data):
        try:
            self.stack.push(data)
        except Exception:
            raise Exception("Queue is full.")


    def dequeue(self):
        if len(self.stack) == 0:
            raise Exception("Queue is empty.")
        i = 0
        while i < len(self.stack)-1:
            self.queue.push(self.stack.pop())
            i+=1
        temp = self.stack.pop()
        while self.queue:
            self.stack.push(self.queue.pop())
        return temp




