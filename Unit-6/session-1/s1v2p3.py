class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next

def find_middle_potion(potions):
	slow = potions
	fast = potions
	
	while fast and fast.next:
	    slow = slow.next
	    fast = fast.next.next
	return slow.potion

potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

print(find_middle_potion(potions1))
print(find_middle_potion(potions2))