def print_todo_list(task):
    print("Pooh's To Dos:")

    # for i in range(len(task)):
    #     print(f"{i+1}. {task[i]}")

    for index, string in enumerate(task, start=1):
        print(f"{index}.{string}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
