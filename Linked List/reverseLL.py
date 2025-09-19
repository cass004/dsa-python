from commons import *

def reverse_ll(head):
    if head is None or head.next is None:
        return head
    
    smallHead = reverse_ll(head.next)
    temp = smallHead
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    head.next = None

    