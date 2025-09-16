from commons import Node, take_input, print_LL

def insert_at_tail(head, value):
    newNode = Node(value)
    if head is None:
        head = newNode
        return head
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    return head

def insert_at_tail_recursive(head, value):
    if head is None:
        newNode = Node(value)
        head = newNode
        return head
    if head.next is None:
        newNode = Node(value)
        head.next = newNode
        return head
    head.next = insert_at_tail_recursive(head.next, value)
    return head

head = take_input()
print_LL(head)
head = insert_at_tail(head, 20)
print_LL(head)
