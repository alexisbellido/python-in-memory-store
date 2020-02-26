import sys
import time
import concurrent.futures
import threading
from store import Store

def retrieve_key(block):
    for i in block:
        key = Store.get(f'num-{i}')
        # print(f'key: num-{i}')

def retrieve_all_keys(blocks):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(retrieve_key, blocks)

if __name__ == "__main__":

    # num = int(input("Enter a number\n"))
    # num = 10000000
    num = 10000000
    num_threads = 5
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
    print('=======================')

    print(f"Retrieving {num:,} keys in multiple threads...")
    keys_per_block = int(num/num_threads)
    blocks = []
    for i in range(num_threads):
        # print(i * keys_per_block, ((i + 1) * keys_per_block))
        blocks.append(range(i * keys_per_block, ((i + 1) * keys_per_block)))

    start_time = time.time()
    retrieve_all_keys(blocks)
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    print(f'Milliseconds elapsed to retrieve each key in {num_threads} threads: {elapsed/num}')
