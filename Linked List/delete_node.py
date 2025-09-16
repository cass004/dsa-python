from commons import Node, take_input, print_LL
head = take_input()

def delete_at_head(head):
    if head is None:
        return None
    newhead = head.next
    return newhead

def delete_at_tail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

def delete_at_tail_recursive(head):
    if head is None or head.next is None:
        return None
    head.next = delete_at_tail_recursive(head.next)
    return head

def delete_at_index(head, index):
    if head is None:
        return None
    if index == 0:
        return head.next
    temp = head
    count = 0
    while temp is not None and count < index-1:
        temp = temp.next
        count+=1
    if temp is None or temp.next is None:
        print("Index out of bounds")
        return head
    nodetobedeleted = temp.next
    nodeafterdeletednode = nodetobedeleted.next if nodetobedeleted is not None else None
    temp.next = temp.next.next
    return head

def delete_at_index_recursive(head, index):
    if head is None:
        return None
    if index == 0:
        return head.next
    head.next = delete_at_index_recursive(head.next, index-1)
    return head

def delete_by_value(head, value):
    if head is None:
        return None
    if head.data == value:
        return head.next
    temp = head
    while temp is not None and temp.next.data !=value:
        temp = temp.next
    temp.next = temp.next.next if temp is not None and temp.next is not None else None
    return head
   
print_LL(head)
head = delete_at_index(head,3)
print_LL(head)