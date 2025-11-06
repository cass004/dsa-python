class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.stack = None
        self.size = 0

    def push(self,data):
        newNode = Node(data)
        if(self.head==None):
            self.head=newNode
            return f"Addded {data} to stack"
        newNode.next=self.head
        self.head=newNode
        self.size+=1
    
    def top(self):
        if(self.head==None or self.size==0):
            return "Stack is empty"
        return self.stack.data
    
    def pop(self):
        if(self.head==None or self.size==0):
            return "Stack is empty"
        poppedNode = self.head
        self.head=self.head.next
        self.size-=1
        return poppedNode.data
    
    def size(self):
        return self.size
    

        
