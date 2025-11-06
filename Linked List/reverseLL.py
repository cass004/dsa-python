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

def reverse_ll_better(head):
    if head is None or head.next is None:
        return head
    
    smallHead = reverse_ll_better(head.next)  
    tailofsmall = head.next
    tailofsmall.next = head
    head.next = None
    return smallHead

def reverse_ll_iterative(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev