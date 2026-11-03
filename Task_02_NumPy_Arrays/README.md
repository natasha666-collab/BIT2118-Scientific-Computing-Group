# Task 2: NumPy Arrays and Numerical Computation

## 1. Objective
To demonstrate how NumPy arrays store numerical data and perform mathematical computations efficiently.

## 2. Concepts Covered
- Creating NumPy arrays using `np.array()`.
- Calculating the mean using `np.mean()`.
- Finding minimum and maximum values using `np.min()` and `np.max()`.
- Performing element-wise arithmetic operations.
- Converting temperatures from Celsius to Fahrenheit.

## 3. Original Problem

A weather station records 24 hourly temperature readings. NumPy is used to calculate the daily mean, minimum and maximum temperatures and convert the readings from Celsius to Fahrenheit.

**Input data:** 24 temperature readings stored in a NumPy array.

**Mathematical operations:**
- Mean: `np.mean(temperatures_c)`
- Minimum: `np.min(temperatures_c)`
- Maximum: `np.max(temperatures_c)`
- Fahrenheit conversion: `F = 1.8C + 32`

**Output interpretation:** The program calculates the average daily temperature, identifies the lowest and highest readings, and converts the first six readings into Fahrenheit.

## 4. Parameter Modification

The original maximum temperature of 29.4°C was changed to 31.4°C.

**Observed changes:**
- Mean temperature increased from approximately 23.12°C to 23.20°C.
- Minimum temperature remained 17.50°C.
- Maximum temperature increased from 29.40°C to 31.40°C.

**Interpretation:** Increasing one reading increased the overall mean slightly. The minimum remained unchanged because the modified reading was not the lowest value.

## 5. Related Real-World Application: Classroom Temperature Monitoring

A university uses five temperature sensors to monitor classroom conditions.

**Input data:** `[24.5, 26.0, 23.8, 28.2, 25.5]` °C.

**Assumptions:**
- All five sensors are functioning correctly.
- All readings are recorded in Celsius.
- The readings represent the same monitoring period.

**Operations performed:**
- Calculation of average temperature.
- Identification of the lowest and highest temperatures.
- Conversion of all readings into Fahrenheit.

**Output interpretation:** The average classroom temperature is 25.60°C. The lowest reading is 23.80°C, while the highest is 28.20°C. These results help illustrate temperature variation within the classroom.

## 6. Files
- `Task_02_numpy_arrays.py` – Original weather station problem.
- `Task_02_real_world.py` – Classroom temperature-monitoring application.
- `README.md` – Explanation, experiments, assumptions and interpretation.

## 7. Conclusion

This task demonstrated how NumPy arrays can store numerical measurements and perform calculations efficiently. It also showed how changing input values affects numerical results and how NumPy can be applied to a practical temperature-monitoring problem.