# Task 20: Monte Carlo

## 1. Original Program
Estimates the probability of a network server overloading under uncertain demand (`code/Task_20_monte_carlo.py`).

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

plt.semilogx(indices + 1, running_probability[indices])
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.grid(True)
plt.show()
```

## 2. Input Values and Mathematical Operations
* **Inputs:** `seed = 42`, `capacity = 1000.0`, `mean_demand` ($\mu = 850.0$), `std_demand` ($\sigma = 120.0$), `N = 100,000`.
* **Operations:**
  1. **Sampling:** Draws $X_i \sim \mathcal{N}(\mu, \sigma^2)$ using `rng.normal()`.
  2. **Threshold Check:** Evaluates $I_i = 1$ if $X_i > 1000.0$, else $0$.
  3. **Probability Estimate:** Computes sample mean $\hat{p} = \frac{1}{N} \sum_{i=1}^{N} I_i$.
  4. **Running Mean:** Computes cumulative average $\hat{p}_k = \frac{1}{k} \sum_{i=1}^{k} I_i$ via `np.cumsum()` to track convergence.

## 3. Parameter Modification
* **Change:** Increased `std_demand` ($\sigma$) from `120.0` to `200.0` (higher traffic volatility).
* **Effect:** Overload probability more than doubles from **~10.56%** to **~22.66%** ($\approx 22,660$ cases). A larger $\sigma$ widens the bell curve, pushing more values past the $1000.0$ limit despite the unchanged mean.

## 4. Output and Interpretation
* **Output Meaning:** There is a **~10.6% chance** that incoming traffic exceeds server capacity ($1000.0$), risking delays or downtime.
* **Graph Interpretation:** On the `semilogx` plot, estimates fluctuate heavily for $N < 100$ due to small sample variance, then flatten around `0.1056` past $N = 10,000$—demonstrating the **Law of Large Numbers**.

## 5. Real-World Application
**Project Budget Overrun Risk:** Simulates uncertain phase costs in a software/construction project to estimate the probability of exceeding an approved budget.

## 6. Assumptions and New Input Data
* **Assumptions:** Phase costs are independent, normally distributed, and sum to total cost ($C_{\text{total}} = C_{\text{labor}} + C_{\text{infra}} + C_{\text{compliance}}$).
* **Inputs:** `seed = 101`, `approved_budget = 5,000,000.0` (KES), `N = 100,000`.
  * **Labor:** $\mu = 2,800,000$, $\sigma = 350,000$
  * **Infrastructure:** $\mu = 1,300,000$, $\sigma = 200,000$
  * **Compliance:** $\mu = 500,000$, $\sigma = 100,000$

## 7. Modified Program and Results
```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(101)
approved_budget = 5_000_000.0
N = 100_000

labor_cost = rng.normal(2_800_000.0, 350_000.0, N)
infra_cost = rng.normal(1_300_000.0, 200_000.0, N)
compliance_cost = rng.normal(500_000.0, 100_000.0, N)

total_cost = labor_cost + infra_cost + compliance_cost
overrun = total_cost > approved_budget

print(f"Expected Total Cost: KES {total_cost.mean():,.2f}")
print(f"Overrun Probability: {overrun.mean():.2%}")
print(f"95th Percentile Cost: KES {np.percentile(total_cost, 95):,.2f}")

running_prob = np.cumsum(overrun) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

plt.semilogx(indices + 1, running_prob[indices], color="darkred")
plt.xlabel("Number of Simulations")
plt.ylabel("Estimated Overrun Probability")
plt.title("Monte Carlo Risk Analysis: Project Budget Overrun")
plt.grid(True)
plt.show()
```

* **Results:** Expected Cost = **KES 4,600,142.50** | Overrun Probability = **16.65%** | 95th Percentile Cost = **KES 5,283,110.00**.
* **Interpretation:** Despite expected costs sitting KES 400k under budget, combined phase variances create a **16.65% overrun risk**. Increasing the budget to **KES 5.28M** keeps overrun risk below 5%.
