# take two pointers, slow and fast
# slow moves 1 step at a time and fast moves two steps
# if slow and fast doesn't meet, then there's no cycle and length is 0
# if they meet, then there's cycle, so fix the fast pointer at the meeting 
# point and move the slow pointer until it meets the fast again and 
# increment a count variable each time to get the length

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return 0    

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))