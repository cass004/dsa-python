class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} to stack ")

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False  
        
    def top(self):
        return self.stack[-1] if not self.is_empty() else None
    
    def pop(self):
        if(self.is_empty(self.stack)):
            print("Stack is empty")
            return None
        return self.stack.pop()
    
    

    


