import numpy as np

# Download latency measurements in milliseconds
download_latency = np.array([20, 35, 50, 80, 100])

# Convert milliseconds into seconds using vectorization
latency_seconds = download_latency / 1000

# Square each latency value
squared_latency = latency_seconds ** 2

# Calculate average latency
average_latency = np.mean(latency_seconds)

# Display results
print("Original latency (ms):", download_latency)
print("Latency in seconds:", latency_seconds)
print("Squared latency:", squared_latency)
print(f"Average latency: {average_latency:.4f} seconds")