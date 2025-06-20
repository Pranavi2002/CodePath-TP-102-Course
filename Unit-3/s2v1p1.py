def manage_stage_changes(changes):
    stack1 = []
    stack2 = []
    for change in changes:
        if change != "Reschedule" and change != "Cancel":
            stack1.append(change[-1])
        elif change == "Cancel":
            c = stack1.pop()
            stack2.append(c)
        else:
            stack1.append(stack2.pop())
    return stack1

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 