import heapq

orders = []

heapq.heappush(orders, (1, 1001, 'Express'))
heapq.heappush(orders, (2, 1002, 'Standard'))

print(heapq.heappop(orders))