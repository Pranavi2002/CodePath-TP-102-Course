from collections import Counter

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

def get_artist_frequency(playlist):
    # artists = []
    # current = playlist
    # while current:
    #     artists.append(current.artist)
    #     current = current.next
    # artist_counts = Counter(artists)
    # print(dict(artist_counts))
    frequency = {}
    current = playlist
    while current:
        frequency[current.artist] = frequency.get(current.artist, 0) + 1
        current = current.next
    print(frequency)

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)