from multiprocessing import Pool
import time

def process_file(file):
    time.sleep(1)
    return f"Processed {file}"

files = ["file1", "file2", "file3"]

with Pool() as pool:
    results = pool.map(process_file, files)

for result in results:
    print(result)