def calculate_average_temperature(temperatures):
    total = sum(temperatures)
    average = total / len(temperatures)
    return average

def calculate_variance(temperatures, average):
    squared_diffs = [(temp - average) ** 2 for temp in temperatures]
    variance = sum(squared_diffs) / len(temperatures)
    return variance

# Prompt the user to enter temperatures for each day of the week
temperatures = []
days_of_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for day in days_of_week:
    temperature = float(input(f"Enter the temperature for {day}: "))
    temperatures.append(temperature)

# Calculate the average temperature for the week
average_temp = calculate_average_temperature(temperatures)
print(f"\nAverage temperature for the week: {average_temp:.2f}")

# Print the highest and lowest temperatures for the week
highest_temp = max(temperatures)
lowest_temp = min(temperatures)
print(f"Highest temperature for the week: {highest_temp}")
print(f"Lowest temperature for the week: {lowest_temp}")

# Sort the temperatures in ascending order
sorted_temperatures = sorted(temperatures)
print("\nTemperatures sorted in ascending order:")
for temp in sorted_temperatures:
    print(temp)

# Calculate the variance of the temperatures for the week
variance = calculate_variance(temperatures, average_temp)
print(f"\nVariance of temperatures for the week: {variance:.2f}")
