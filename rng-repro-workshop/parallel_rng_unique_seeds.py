import numpy as np
import multiprocessing

def generate_random_numbers(worker_id):
    # Unique seed per worker
    rng = np.random.default_rng(42 + worker_id)
    print(f"Worker {worker_id}: {rng.random(3)}")

if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    pool.map(generate_random_numbers, range(4))