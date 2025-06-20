from collections import deque

def count_explorers(explorers, supplies):
    queue = deque(explorers)
    stack = supplies
    i = 0  # pointer for the top of the supply stack

    # We'll keep track of how many explorers have been rotated without any supply taken
    # If this equals the queue length, it means no one wants the current supply
    rotations = 0

    while queue and i < len(stack):
        if queue[0] == stack[i]:
            queue.popleft()   # explorer takes the supply and leaves
            i += 1            # move to the next supply
            rotations = 0     # reset rotations since a supply was taken
        else:
            queue.append(queue.popleft())  # move explorer to the back
            rotations += 1

            # If all remaining explorers have been rotated once without success, stop
            if rotations == len(queue):
                break

    return len(queue)

print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  
print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) 