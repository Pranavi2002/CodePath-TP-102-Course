def validate_nft_actions(actions):
    # egde case where actions is empty
    if len(actions) == 0:
        return True
    count = []
    for action in actions:
        if action == "add":
            count.append(action)
        else:
            if not len(count):
                return False
            else:
                count.pop()
    return len(count) == 0  #O(n) TC, O(n) SC

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))