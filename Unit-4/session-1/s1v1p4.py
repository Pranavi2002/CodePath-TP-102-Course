def average_nft_value(nft_collection):
    if not nft_collection:  #O(1) TC
        return 0 
    sum_value = 0   #O(1) TC, O(1) SC
    n = len(nft_collection) #O(1) TC, O(1) SC 
    for nft in nft_collection:  #O(n) TC
        sum_value += nft["value"]   #O(1) TC, O(n) SC
    return sum_value/n

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))