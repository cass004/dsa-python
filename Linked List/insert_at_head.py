from commons import Node, take_input, print_LL

head = take_input()

print_LL(head)

def insert_at_head(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head

head = insert_at_head(head, 10)
print_LL(head)