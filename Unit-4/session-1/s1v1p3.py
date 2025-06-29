from collections import Counter, defaultdict

def identify_popular_creators(nft_collection):
    nft_creaters = Counter(nft["creator"] for nft in nft_collection) # O(n) TC, O(k) SC
    popular_creators = [creator for creator, count in nft_creaters.items() if count > 1] # O(n) TC, worst-case O(k) SC
    return popular_creators

    #way-2:
    # res = []
    # freq = defaultdict(int)
    # for nft in nft_collection:
    #     if nft['creator'] in freq:
    #         res.append(nft['creator'])
    #     freq[nft['creator']] += 1
    # return res  

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))