class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# def find_min(head):
#     minVal = head.value
#     while head:
#         if minVal > head.value:
#             minVal = head.value
#         head = head.next
#     return minVal

def find_min(head):
    curr = head
    minVal = curr.value
    while curr:
        if minVal > curr.value:
            minVal = curr.value
        curr = curr.next
    return minVal

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))