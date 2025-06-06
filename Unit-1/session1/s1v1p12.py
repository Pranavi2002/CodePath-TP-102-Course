def locate_thistles(items):
    ans = []
    for i in range(len(items)):
        if items[i] == "thistle":
            ans.append(i)
    print(ans)

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)