import numpy as np

# Temperature readings collected from five classroom sensors
classroom_temps = np.array([24.5, 26.0, 23.8, 28.2, 25.5])

# Calculate temperature statistics
average = np.mean(classroom_temps)
minimum = np.min(classroom_temps)
maximum = np.max(classroom_temps)

# Convert Celsius readings to Fahrenheit
fahrenheit = (1.8 * classroom_temps) + 32

# Display results
print("Classroom temperature readings:", classroom_temps)
print(f"Average temperature: {average:.2f} °C")
print(f"Lowest temperature: {minimum:.2f} °C")
print(f"Highest temperature: {maximum:.2f} °C")
print("Temperatures in Fahrenheit:", fahrenheit)