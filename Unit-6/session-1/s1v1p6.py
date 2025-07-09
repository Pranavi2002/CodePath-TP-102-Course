# Skip the first node (head) — it's not considered a critical point.
# Use a three-pointer traversal:
# prev: the previous node,
# curr: the current node (potential critical point),
# next: the node after curr.
# Traverse the list from the second node to the second-to-last node (ignoring head and tail).
# At each step:
# Check if curr is a local minima:
# prev.val > curr.val < next.val
# Check if curr is a local maxima:
# prev.val < curr.val > next.val
# If either condition is true, increment a counter for critical points.
# Continue moving all three pointers forward until next is None (i.e., curr is the second-to-last node).

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

def count_critical_points(song_audio):
    # prev = song_audio
    # curr = prev.next
    # next_node = curr.next
    prev = song_audio
    current = song_audio.next
    next_node = song_audio.next.next
    count = 0
    while current.next:
        if current.value < prev.value and current.value < next_node.value:
            count += 1
        elif current.value > prev.value and current.value > next_node.value:
            count += 1
        prev = current
        current = next_node
        next_node = next_node.next
    return count

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))

