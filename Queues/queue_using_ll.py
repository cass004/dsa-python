class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def size(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0
    
    def enqueue(self, data):
        newNode = Node(data)
        self.length += 1
        if self.read is None:
            self.front = newNode
            self.rear = newNode
            print(f"Enqueued {data} to queue")
            return
        else:
            self.rear.next = newNode
            self.rear = newNode

        print(f"Enqueued {data} to queue")

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        dequeuedNode = self.front
        self.front = self.front.next
        self.length -= 1
        return dequeuedNode.data
        if (self.front is None):
            self.rear = None