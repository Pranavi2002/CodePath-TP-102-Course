def tiggerfy(s):
    remove_letters = {'t', 'i', 'g', 'e', 'r'}
    return '"' + ''.join(c for c in s if c.lower() not in remove_letters) + '"'

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))