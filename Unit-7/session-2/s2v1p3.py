# def count_checked_in_passengers(rooms):
#     low = 0
#     high = len(rooms) - 1
#     first_ind = len(rooms)
#     while low <= high:
#         mid = (low + high) // 2
#         if rooms[mid] == 1:
#             first_ind = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return len(rooms) - first_ind

def count_checked_in_passengers(rooms):
    l,r = 0,len(rooms) -1
    while l<r:
        mid = (r+l)//2
        if rooms[mid] == 0:
            l=mid+1
        elif rooms[mid] == 1:
            r=mid
    if rooms[l] == 0:
        return 0
    else:
        return len(rooms) -l

rooms1 = [0, 0, 0, 1, 1, 1, 1]
# low = 0
# high = 6
# mid = 3
# 1
# high = 3
# mid = 1
# f = 1 
# 0
# low = 2
# mid = 2
# low = 3
# low == high: len - low

rooms2 = [0, 0, 0, 0, 0, 1]
# low = 0
# high = 5
# mid = 2
# 0
# low = 3
# mid = 4
# 0
# low = 5
# low == high:

rooms3 = [0, 0, 0, 0, 0, 0]
# low = 0
# high = 5
# mid = 2
# 0
# low = 3
# mid = 4
# 0
# low = 5
# low == high:  

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))