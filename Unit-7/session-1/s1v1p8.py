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

# def merge_missions(mission1, mission2):
#     # code to combine two lists
#     curr = mission1
#     while curr.next:
#         curr = curr.next
#     curr.next = mission2
#     return merge_sort(mission1)
#     # return mission1

# # Function to merge two sorted linked lists
# def merge_lists(l1, l2):
#     dummy = Node(0)
#     tail = dummy

#     while l1 and l2:
#         if l1.value < l2.value:
#             tail.next = l1
#             l1 = l1.next
#         else:
#             tail.next = l2
#             l2 = l2.next
#         tail = tail.next

#     # Append the remaining nodes
#     tail.next = l1 if l1 else l2
#     return dummy.next

# # Function to split the linked list into two halves
# def get_middle(head):
#     if head is None or head.next is None:
#         return head

#     slow = head
#     fast = head
#     prev = None

#     while fast and fast.next:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next

#     # Disconnect the first half from the second
#     if prev:
#         prev.next = None

#     return slow

# # Merge sort on a linked list
# def merge_sort(head):
#     if head is None or head.next is None:
#         return head

#     middle = get_middle(head)
#     left = merge_sort(head)
#     right = merge_sort(middle)

#     return merge_lists(left, right)

# Recursive Approach
def merge_missions_recursive(mission1, mission2):
    # Base cases
    if mission1 is None:
        return mission2
    if mission2 is None:
        return mission1

    if mission1.value < mission2.value:
        mission1.next = merge_missions_recursive(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions_recursive(mission1, mission2.next)
        return mission2
    
# Iterative Approach
def merge_missions_iterative(mission1, mission2):
    dummy = Node(0)
    tail = dummy

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return dummy.next


mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions_recursive(mission1, mission2))
print_linked_list(merge_missions_iterative(mission1, mission2))