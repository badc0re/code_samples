from service.client import SolverClient
from multiprocessing.pool import ThreadPool
from itertools import product


def wrapper(args):
    return sc.ackermann_recursive(*args)


NUM_WORKER_THREADS = 35
test_ranges = range(1, 100)
test_pairs_ackermann = []

for i in range(0, 3):
    for j in range(0, 1):
        test_pairs_ackermann.append((i, j))


sc = SolverClient("127.0.0.1", 8000)
print("Starting integration tests..")
print(f"Spawning NUM_WORKER_THREADS {NUM_WORKER_THREADS}")
pool = ThreadPool(NUM_WORKER_THREADS)

fib_results = pool.map_async(sc.fibbonachi, test_ranges)
print(fib_results.get())

fac_results = pool.map_async(sc.factorial, test_ranges)
print(fac_results.get())

ackermann_results = pool.map_async(wrapper, test_pairs_ackermann)
print(ackermann_results.get())
pool.close()
