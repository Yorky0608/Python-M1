import multiprocessing
import random
import time
from datetime import datetime

def worker():
    """wait a random 0‑1 s, print the current clock and return."""
    delay = random.random()  # float in [0.0, 1.0)
    time.sleep(delay)
    print(f"process {multiprocessing.current_process().name}:", datetime.now())

if __name__ == "__main__":
    procs = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"p{i+1}")
        p.start()
        procs.append(p)

    # wait for all of them to finish before exiting main program
    for p in procs:
        p.join()

