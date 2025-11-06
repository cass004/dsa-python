from commons import *

def merge_two_sorted_ll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalHead = None
    finalTail = None
    
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if finalHead is None:
                finalHead = head1
                finalTail = head1
            else:
                finalTail.next = head1
                finalTail = head1
            head1 = head1.next
        else:
            if finalHead is None:
                finalHead = head2
                finalTail = head2
            else:
                finalTail.next = head2
                finalTail = head2
            head2 = head2.next
    if head1 is not None:
        finalTail.next = head1
    if head2 is not None:
        finalTail.next = head2
    return finalHead



