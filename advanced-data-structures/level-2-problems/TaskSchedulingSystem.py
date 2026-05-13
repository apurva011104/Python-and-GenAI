import heapq

tasks = [(2, "Low"), (1, "High"), (3, "Medium")]

heapq.heapify(tasks)

priority, task = heapq.heappop(tasks)

print("Processing:", task)