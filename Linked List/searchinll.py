from commons import Node, take_input, print_LL

def createfrom_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

head = createfrom_list([3,4,5,2,6,1,9])

def search_by_value(head, value):
    temp = head
    index = 0
    while temp is not None:
        if temp.data == value:
            return index
        temp = temp.next
        index+=1
    return -1