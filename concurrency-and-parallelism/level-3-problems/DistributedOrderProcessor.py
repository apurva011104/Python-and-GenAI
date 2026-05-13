from multiprocessing import Process, Queue

def worker(queue):
    while not queue.empty():
        order = queue.get()
        print(f"Processed {order}")

if __name__ == "__main__":
    orders = ["Order1", "Order2", "Order3"]

    queue = Queue()

    for order in orders:
        queue.put(order)

    processes = []

    for _ in range(3):
        p = Process(target=worker, args=(queue,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()