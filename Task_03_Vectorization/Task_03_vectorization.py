import numpy as np
import timeit

# Generate one million network latency measurements
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 100_000)
# Using a traditional loop
def loop_version():
    squared = []

    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared

# Using NumPy vectorization
def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

# Compare execution times
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

result = vectorized_version()

print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} seconds")
print(f"Vectorized time: {vector_time:.4f} seconds")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")