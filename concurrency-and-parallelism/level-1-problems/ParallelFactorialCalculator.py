from multiprocessing import Pool
import math

numbers = [5, 7, 10]

with Pool() as pool:
    results = pool.map(math.factorial, numbers)

for result in results:
    print(result)