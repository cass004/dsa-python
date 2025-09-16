from commons import Node, take_input, print_LL  

head = take_input()
print_LL(head)
def insert_at_head(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head
def insert_at_index(head, index, value):
    if (index == 0):
        return insert_at_head(head, value)
    newNode = Node(value)
    temp = head
    count = 0
    while temp is not None and count < index - 1:
        temp = temp.next
        count += 1
    if temp is None:
        return head
    newNode.next = temp.next
    temp.next = newNode
    return head

def insert_at_index_recursive(head, index, value):
    if index == 0:
        return insert_at_head(head, value)
    if head is None:
        print("Index out of bounds")
        return head
    head.next = insert_at_index_recursive(head.next, index - 1, value)
    return head

head = insert_at_index(head, 3, 35)
print_LL(head)