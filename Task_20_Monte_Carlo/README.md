Task 20: Random Numbers and Monte Carlo Methods
1. Objective
 To demonstrate how random number generation and Monte Carlo simulations estimate probabilities and model uncertainty in complex systems.
2. Concepts Covered
  •	Initializing a reproducible random number generator using np.random.default_rng().
  •	Sampling from normal distributions using rng.normal().
  •	Evaluating threshold conditions using boolean comparisons.
  •	Estimating probabilities using sample means (.mean()).
  •	Tracking convergence using cumulative sums (np.cumsum()) and logarithmic plots (plt.semilogx()).
3. Original Problem
 A network server experiences fluctuating user demand. Monte Carlo simulation is used to estimate the probability that incoming demand exceeds the server's maximum size.
  •	Input data: seed = 42, capacity = 1000.0, mean_demand = 850.0, std_demand = 120.0, N = 100,000 simulations.
  •	Mathematical operations:
    o	Normal sampling: $X_i \sim \mathcal{N}(850.0, 120.0^2)$ 
    o	Overload check: overloaded = demand > capacity
    o	Probability estimate: $\hat{p} = \frac{1}{N} \sum I_i$ (overloaded.mean())
    o	Running convergence: np.cumsum(overloaded) / np.arange(1, N + 1)
  •	Output interpretation: The program estimates a 10.62% probability of server overload (10,619 cases out of 100,000). The convergence plot shows early fluctuations
    stabilizing around 0.1062 as $N$ increases, illustrating the Law of Large Numbers.
5. Parameter Modification
 The demand standard deviation (std_demand) was increased from 120.0 to 200.0 to simulate higher traffic volatility.
  •	Observed changes:
    o	Estimated overload probability increased from 10.62% to 22.60%.
    o	Overload cases rose from 10,619 to 22,603 out of 100,000 simulations.
  •	Interpretation: Increasing variability widens the normal distribution curve, pushing a much larger portion of random demand spikes past the 1000.0 capacity limit         even   though the average demand remained unchanged.
6. Related Real-World Application: Project Budget Overrun Risk
 A project management team wants to estimate the probability that a project exceeds its approved budget when phase costs are uncertain.
  •	Input data: approved_budget = KES 5,000,000, N = 100,000 simulations.
    o	Labor cost: Mean = KES 2,800,000, Std Dev = KES 350,000
    o	Infrastructure cost: Mean = KES 1,300,000, Std Dev = KES 200,000
    o	Compliance cost: Mean = KES 500,000, Std Dev = KES 100,000
  •	Assumptions:
    o	All three phase costs are independent and normally distributed.
    o	Total project cost is the sum of the three phase costs.
    o	No mid-project scope changes occur.
  •	Operations performed:
    o	Simulating random costs for each phase and summing them (total_cost).
    o	Calculating expected total cost, overrun probability (total_cost > approved_budget), and the 95th percentile cost (np.percentile()).
  •	Output interpretation: The expected total cost is KES 4,600,142.50, with a 16.89% probability of exceeding the KES 5.0M budget. The 95th percentile cost is KES           5,283,110.00, indicating that allocating KES 5.28M keeps overrun risk below 5%.
7. Files
  •	Task_20_monte_carlo.py – Original server-overload risk simulation.
  •	Task_20_project_budget_mc.py – Project budget overrun risk application.
•	README.md – Explanation, experiments, assumptions, and interpretation.
8. Conclusion
