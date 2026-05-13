from multiprocessing import Pool
import time

def process_csv(file):
    time.sleep(1)
    print(f"Cleaning {file}")
    return f"{file} processed"

files = ["sales.csv", "marketing.csv", "finance.csv"]

with Pool() as pool:
    results = pool.map(process_csv, files)

print("All data merged successfully.")