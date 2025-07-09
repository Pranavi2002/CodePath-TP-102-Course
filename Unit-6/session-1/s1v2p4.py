# take three pointers:
# prev = None, curr = head, next_node = head.next
# loop until end of list ( curr becomes None):
# next_node = curr.next, curr.next = prev, prev = curr, curr = next_node
# return prev, as it will be the new head 

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

def reverse(events):
    prev = None
    curr = events
    next_node = events.next
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))
