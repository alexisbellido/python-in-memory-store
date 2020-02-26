import sys
import time
from store import Store

if __name__ == "__main__":

    # num = int(input("Enter a number\n"))
    num = 10000000
    # num = 1000
    print(f"Storing {num:,} keys...")

    start_time = time.time()

    for i in range(num):
        Store.set(f'num-{i}', i)
        # print(Store.set(f'num-{i}', i))

    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    print(f'Keys stored: {num:,}')
    print(f'Milliseconds per key: {elapsed/num}')

    bytes_used = sys.getsizeof(Store._store)
    print(f'Bytes used by store: {bytes_used:,}')
    print(f'Bytes used per key: {bytes_used/num:,}')

    print(f"Retrieving {num:,} keys...")

    start_time = time.time()

    for i in range(num):
        key = Store.get(f'num-{i}')
        # print(f'num-{i}: {key}')

    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    print(f'Milliseconds elapsed to retrieve each key: {elapsed/num}')
