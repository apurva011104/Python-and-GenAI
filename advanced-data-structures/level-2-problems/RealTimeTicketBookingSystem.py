import heapq

tickets = []

heapq.heappush(tickets, (3, "Regular"))
heapq.heappush(tickets, (1, "VIP"))

priority, customer = heapq.heappop(tickets)

print("Processing", customer)