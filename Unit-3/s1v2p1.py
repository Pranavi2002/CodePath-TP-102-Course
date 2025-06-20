from collections import deque

def time_required_to_stream(movies, k):
    q = deque()
    time = 0
    
    # Initialize queue with (index, remaining_time)
    for i in range(len(movies)):
        q.append((i, movies[i]))
    
    while q:
        i, remaining = q.popleft()
        # Process one unit of streaming time
        remaining -= 1
        time += 1
        
        if i == k and remaining == 0:
            return time  # Finished streaming movie k
        
        # If movie still needs streaming, put it back at the end
        if remaining > 0:
            q.append((i, remaining))

print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 