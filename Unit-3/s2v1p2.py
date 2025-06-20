def process_performance_requests(requests):
    
    # Sort by priority descending, then by arrival order (which is preserved automatically)
    # sorted_requests = sorted(requests, key=lambda x: x[0], reverse=True)
    sorted_requests = sorted(requests, key=lambda x: -x[0])
    
    queue = []
    for priority, event in sorted_requests:
        queue.append(event)
    
    return queue

    # #using priority queue
    # import heapq

    # heap = []
    # order = []
    
    # for idx, (priority, event) in enumerate(requests):
    #     # Push negative priority to simulate max-heap
    #     heapq.heappush(heap, (-priority, idx, event))
    
    # while heap:
    #     _, _, event = heapq.heappop(heap)
    #     order.append(event)
    
    # return order


print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))