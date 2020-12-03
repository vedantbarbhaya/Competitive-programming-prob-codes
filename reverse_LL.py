# one pass solution to reverse a singly linked list
def reverse_ll(head):

    if head == None or head.next!= None:
        return head

    reversed_list = head
    remaining_list_head = head.next

    while(remaining_list_head != None):

        temp = remaining_list_head
        temp.next = reversed_list
        remaining_list_head = remaining_list_head.next
        reversed_list = temp

    return reversed_list
