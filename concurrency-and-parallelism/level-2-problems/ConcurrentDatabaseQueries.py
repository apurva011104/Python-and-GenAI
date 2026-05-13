import threading
import time

def query_database(db):
    print(f"Querying {db}...")
    time.sleep(2)

databases = ["DB1", "DB2", "DB3"]

threads = []

for db in databases:
    t = threading.Thread(target=query_database, args=(db,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All queries completed.")