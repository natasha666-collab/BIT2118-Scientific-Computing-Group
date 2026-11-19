import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define parameters
capacity = 1000.0   # Server capacity
mean_demand = 850.0  # Average demand
std_demand = 120.0   # Demand standard deviation
N = 100000          # Number of simulations

# Step 2: Generate random demand using a normal distribution
np.random.seed(42)  # Set seed for reproducible results
demand = np.random.normal(mean_demand, std_demand, N)

# Step 3: Identify overload cases (demand > capacity)
overloaded = demand > capacity
overload_probability = np.mean(overloaded)

print(f"Total Simulations: {N}")
print(f"Overload Count: {np.sum(overloaded)}")
print(f"Estimated Overload Probability: {overload_probability:.4%}")

# Step 4: Calculate running probability to observe convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Step 5: Plot the convergence results
plt.figure(figsize=(8, 4.5))
plt.plot(running_probability, label='Running Probability', color='blue')
plt.axhline(overload_probability, color='red', linestyle='--', label=f'Final Probability ({overload_probability:.2%})')

plt.xscale('log')  # Logarithmic scale for better visualization of convergence
plt.xlabel('Number of Simulations (Log Scale)')
plt.ylabel('Overload Probability')
plt.title('Monte Carlo Simulation: Server Overload Probability')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()
