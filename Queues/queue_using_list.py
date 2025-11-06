class QueueUsingList:
    def __init__(self):
        self.__queue = []
    
    def size(self):
        return len(self.__queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self, data):
        self.__queue.append(data)
        print(f"Enqueued {data} to queue")

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.__queue[0]
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.__queue.pop(0)
    

Q = QueueUsingList()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
print("Front element is:", Q.front())
print(Q.size())

