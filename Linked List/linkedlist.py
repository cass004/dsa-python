class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

head = first    #point to the first node

def print_LL(head):
    while(head != None):
        print(head.data)
        head = head.next
    return

print_LL(head)
