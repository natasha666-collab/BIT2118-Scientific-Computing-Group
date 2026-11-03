# Task 3: Mathematical Functions and Vectorization

## 1. Objective

To demonstrate how mathematical operations can be applied to multiple numerical values simultaneously using NumPy vectorization, and compare its performance with traditional Python loops.

## 2. Concepts Covered

- Mathematical functions and operations.
- NumPy vectorization.
- Element-wise arithmetic.
- Conversion of units.
- Execution-time measurement using `timeit`.
- Comparison of loop-based and vectorized computation.

## 3. Original Problem

A network-monitoring system contains one million latency measurements recorded in milliseconds. The program converts each measurement into seconds and squares the resulting values.

**Input data:** One million randomly generated latency measurements between 5 ms and 250 ms, using a fixed random seed of 42.

**Mathematical operations:**

- Conversion to seconds: `seconds = latency_ms / 1000.0`
- Squaring: `squared = seconds ** 2`

**Methods used:**
- Traditional Python loop.
- NumPy vectorized operations.

**Output interpretation:** The program displays the first five squared latency values and compares the execution times of both methods.

## 4. Parameter Modification Experiment

The dataset size was reduced from 1,000,000 to 100,000 measurements.

### Results comparison

| Measurement | 1,000,000 values | 100,000 values |
|---|---:|---:|
| Loop time | 0.9420 seconds | 0.0286 seconds |
| Vectorized time | 0.0067 seconds | 0.0010 seconds |
| Approximate speed-up | 140.3x | 29.0x |

**Interpretation:** Reducing the dataset size decreased the execution time of both methods. The vectorized method remained faster than the traditional loop. The speed-up changed because relative performance depends on dataset size and execution conditions.

The first five values remained unchanged because the random number generator used the same seed.

## 5. Related Real-World Application: Campus Network Latency Analysis

A university wants to analyse download latency measurements from its campus network.

**Input data:** `[20, 35, 50, 80, 100]` milliseconds.

**Assumptions:**
- All measurements are valid.
- All readings are recorded in milliseconds.
- The five measurements represent observations from the campus network.

**Mathematical operations:**
- Convert milliseconds into seconds.
- Square each latency value.
- Calculate average latency.

**Output:**
- Latency in seconds: `[0.02, 0.035, 0.05, 0.08, 0.1]`
- Squared latency: `[0.0004, 0.001225, 0.0025, 0.0064, 0.01]`
- Average latency: `0.0570 seconds`.

**Interpretation:** The average download latency is 0.057 seconds, equivalent to 57 milliseconds. The squared values provide transformed measurements that can be used in further numerical analysis.

## 6. Files

- `Task_03_vectorization.py` – Original network latency problem and execution-time comparison.
- `Task_03_real_world.py` – Campus network latency application.
- `README.md` – Explanation, experiments, assumptions and interpretation.

## 7. Conclusion

This task demonstrated how NumPy vectorization applies mathematical operations to multiple values simultaneously. The execution-time experiment showed that vectorization was significantly faster than the traditional loop for the tested datasets. The real-world application demonstrated how vectorization can support network latency analysis.