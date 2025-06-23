def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for c in vip_passes:
        vip_set.add(c)
    vip_guests = 0
    for c in guests:
        if c in vip_set:
            vip_guests += 1
    return vip_guests

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))