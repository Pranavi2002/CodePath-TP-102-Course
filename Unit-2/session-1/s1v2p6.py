def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    trans = set(transmission)
    return alphabets.issubset(trans)

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))