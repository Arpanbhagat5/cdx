class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None
def print_list(head: Node) -> None:
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def reverse_list(head: Node) -> Node:
    print_list(head)
    if head is None:
        return

    prev = None
    next = head.next

    while next is not None:
        head.next = prev
        prev = head
        head = next
        next = next.next
    head.next = prev
    prev = head

    # print list
    print_list(head)

    return head


list1 = Node('A')
list1.next = Node('B')
list1.next.next = Node('C')
list1.next.next.next = Node('D')
list1.next.next.next.next = Node('E')
list1.next.next.next.next.next = Node('F')

reverse_list(list1)
