class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# print_linked_list(top_hits_2010s)

node1 = SongNode("Uptown Funk")
node2 = SongNode("Party Rock Anthem")
node3 = SongNode("Bad Romance")
node1.next = node2
node2.next = node3
node3.next = None

print_linked_list(node1)

