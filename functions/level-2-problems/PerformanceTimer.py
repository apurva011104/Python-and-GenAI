import time


def measure_time(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()

    execution_time_ms = (end_time - start_time) * 1000
    print(f"Execution time: {execution_time_ms:.2f} ms")


measure_time(lambda: sum(range(100000)))
