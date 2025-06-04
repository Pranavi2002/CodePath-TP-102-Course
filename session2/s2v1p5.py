def final_value_after_operations(operations):
    trigger = 1
    for word in operations:
        if word == "bouncy" or word == "flouncy":
            trigger += 1
        if word == "trouncy" or word == "pouncy":
            trigger -= 1
    print(trigger)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)