def is_prefix_of_signal(transmission, searchSignal):
    words = transmission.split()
    c = 0
    for word in words:
        c += 1
        if searchSignal in word:
            return c
    return -1

print(is_prefix_of_signal("i love eating burger", "burg")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you"))
