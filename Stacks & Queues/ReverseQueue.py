from DinamicArrayQueue import DinamicArrayQueue
from DinamicArrayStack import DinamicArrayStack

def reverseQueue(q):
    s = DinamicArrayStack()
    while q:
        s.push(q.dequeue())
    while s:
        q.enqueue(s.pop())
    return q

q = DinamicArrayQueue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)

print(reverseQueue(q).front())