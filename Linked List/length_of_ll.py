from commons import Node, take_input, print_LL
def length_of_LL(head):
    temp = head
    ans = 0
    while temp is not None:
        ans += 1
        temp = temp.next
    return ans

new_head = take_input()
len_of_list = length_of_LL(new_head)
print(len_of_list)
