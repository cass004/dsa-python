class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
    return

def take_input():
    print("Enter node values. Enter -1 to stop.")
    value = int(input("Enter the value of node: "))
    head = None
    tail = None

    while value != -1:
        newNode = Node(value)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter the value of node: "))
    return head

new_head = take_input()
print("\nYour Linked List:")
print_LL(new_head)