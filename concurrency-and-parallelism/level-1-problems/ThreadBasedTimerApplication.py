import threading
import time

def timer():
    for _ in range(3):
        print("System alive...")
        time.sleep(2)

thread = threading.Thread(target=timer)
thread.start()

thread.join()