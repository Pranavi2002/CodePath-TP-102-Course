def get_item(items, x):
    if x > len(items):
        return None
    else:
        return items[x]

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))  # Expected output: "roo"

x = 5
print(get_item(items, x))  # Expected output: None
